#Create a base class Person, derived class CrewMember, and a further derived class Pilot.
#-Person contains name and ID.
#-CrewMember adds role (e.g., "Cabin Crew", "Pilot").
#-Pilot adds license number and rank (e.g., "Captain").

class Person:
        def __init__(self, name, id):
            self.name = name
            self.id = id

        def showDetails(self):
              print(f"Name:{self.name}, ID: {self.id}")

class CrewMember(Person):
        def __init__(self, name, id, role):
            super().__init__(name,id)
            self.role = role

        def showRole(self):
              print(f"Role:{self.role}")

class Pilot(CrewMember):
        def __init__(self, name, id, role, license_no, rank):
            CrewMember.__init__(self, name, id, role)
            self.license_no = license_no
            self.rank = rank

        def showPilotDetails(self):
              self.showDetails()
              self.showRole()
              print(f"License No:{self.license_no}, Rank: {self.rank}")


      
e = Pilot("Ram", "123456789", "Cabin Crew", "LIC123456", "200")
e.showPilotDetails()
