from rest_framework.decorators import api_view
from .decorator import is_admin, is_authenticated_custom
from .models import Ticket
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from django.db.models import Q
from .serializers import TicketSerializer
from django.core.exceptions import ObjectDoesNotExist
from .exceptions import (
    http_401_unauthorized,
    http_404_not_found,
    http_500_internal_server_error,
)

User = get_user_model()


@is_admin
@api_view(["POST"])
def create_ticket(request):
    try:
        title = request.POST.get("title")
        description = request.POST.get("description")
        employee_id = int(request.POST.get("employee_id"))

        employee = User.objects.get(id=employee_id)

        new_ticket = Ticket(title=title, description=description, assignedTo=employee)
        new_ticket.save()

        return Response({"ticket_id": new_ticket.id})

    except ObjectDoesNotExist as e:
        print(str(e))
        raise http_404_not_found()

    except Exception as e:
        print(str(e))
        raise http_500_internal_server_error()


@is_authenticated_custom
@api_view(["GET"])
def get_tickets(request):
    try:
        status_acronym = {
            "open": "O",
            "close": "C",
        }
        priority_acronym = {
            "low": "L",
            "medium": "M",
            "high": "H",
        }

        status = request.GET.get("status")
        status = status_acronym.get(status)

        priority = request.GET.get("priority")
        priority = priority_acronym.get(priority)

        title = title if request.GET.get("title") else []

        tickets = Ticket.objects.filter(
            Q(status=status) | Q(priority=priority) | Q(title__icontains=title)
        )

        serializer = TicketSerializer(tickets, many=True)

        return Response(serializer.data)

    except Exception as e:
        print(str(e))
        raise http_500_internal_server_error()


@is_authenticated_custom
@api_view(["GET"])
def get_tickets_all(request):
    try:
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)

    except Exception as e:
        print(str(e))
        raise e


# Helper for checking priorities
def is_high_priority(current, other):
    if current == "H":
        return False
    
    if current == "M" and other == "H":
        return True

    if current == "L" and (other == "M" or other == "H"):
        return True

    return False


@is_authenticated_custom
@api_view(["POST"])
def close_ticket(request):
    try:
        ticket_id = request.POST.get("ticket_id")
        ticket = Ticket.objects.get(id=ticket_id)

        current_ticket_priority = ticket.priority

        employee = ticket.assignedTo

        ticket_of_employee = Ticket.objects.filter(assignedTo=employee)

        high_tickets = []
        for t in ticket_of_employee:
            if is_high_priority(current_ticket_priority, t.priority):
                high_tickets.append(t)

        if high_tickets:
            serializer = TicketSerializer(high_tickets, many=True)
            return Response({"message": "A higher priority task remains to be closed",
                "tickets": serializer.data
                })

        ticket.status = "C"
        ticket.save()

        serializer = TicketSerializer(ticket)
        return Response(serializer.data)

    except ObjectDoesNotExist as e:
        print(str(e))
        raise http_404_not_found()

    except Exception as e:
        print(str(e))
        raise e


@is_admin
@api_view(["POST"])
def delete_ticket(request):
    try:
        ticket_id = int(request.POST.get("ticket_id"))

        ticket = Ticket.objects.get(id=ticket_id)
        ticket.delete()

        return Response({"message": f"{ticket_id} - deleted successfuly"})

    except ObjectDoesNotExist as e:
        print(str(e))
        raise http_404_not_found()

    except Exception as e:
        print(str(e))
        raise e
