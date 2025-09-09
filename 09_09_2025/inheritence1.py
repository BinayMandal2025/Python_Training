#Create a base class Flight with basic flight information. Create a derived class ScheduledFlight that adds scheduling information.
 
#Requirements:
#-Flight should have attributes: flight number, airline.
#-ScheduledFlight should add departure time and arrival time.
#-Include methods to display complete flight information.


class Flight:
        def __init__(self, flight_number, airline):
            self.flight_number = flight_number
            self.airline = airline

        def showFlightDetails(self):
              print(f"Flight Number:{self.flight_number}, Ariline: {self.airline}")

class ScheduledFlight(Flight):
        def __init__(self, flight_number, airline, dept_time, arr_time):
            super().__init__(flight_number,airline)
            self.dept_time = dept_time
            self.arr_time = arr_time

        def showDetails(self):
            self.showFlightDetails()
            print(f"Dept Time: {self.dept_time}, Arival Time: {self.arr_time}")
      
e = ScheduledFlight("AI101", "Air India", "10:22", "13:20")
e.showDetails()
