#Create one class PassengerDetails and another class TicketDetails. Create a new class Booking that inherits from both.
#Requirements:
#- PassengerDetails has name, age.
#- TicketDetails has ticket number, seat number.
#- Booking shows all information.
class PassengerDetails:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def PassengerDetails(self):
              print(f"Name:{self.name}, ID: {self.age}")

class TicketDetails:
        def __init__(self, ticket_number, seat_number):
            self.ticket_number = ticket_number
            self.seat_number = seat_number

        def TicketDetails(self):
              print(f"Ticket Number:{self.ticket_number}, Seat Number: {self.seat_number}")

class Booking(PassengerDetails, TicketDetails):
        def __init__(self, name, age, ticket_number, seat_number):
            PassengerDetails.__init__(self, name, age)
            TicketDetails.__init__(self, ticket_number, seat_number)

        def showBookingDetails(self):
              self.PassengerDetails()
              self.TicketDetails()

e = Booking("Ram", "45", "AI10003", 12)
e.showBookingDetails()
