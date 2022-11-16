import random

# Name: Jayson Yin
# Your assignment for today is to create a parking garage class to get more familiar with Object Oriented Programming(OOP). 

tickets =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
parkingSpaces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
current_ticket = {}

class ParkingGarage():

    def __init__(self, tickets, spaces, current_ticket):
        self.tickets = tickets
        self.spaces = spaces
        self.current_ticket = current_ticket
    
    # This method will decrease the amount of tickets availible by 1
    # And also the amount of parking spaces by one
    def takeTicket(self):
        ticket = self.tickets.pop()
        space = self.spaces.pop()
        self.current_ticket[f'ticket {ticket}'] = 'not paid'
        print(f"You have taken ticket {ticket} please report to parking space {space}.") # Both use the same index, thus the tickets correlate with the spot
    
    # This method allows you to pay for a ticket
    # The value of the ticket will be set to paid
    def payForParking(self):
        print("Here is the open ticket:")
        for key in self.current_ticket.keys():
            print(f"\t{key.title()}")
        answer = input("Please enter ('y') to proceed with payment: ")
        if answer.lower() == 'y':
            for key in self.current_ticket.keys():
                self.current_ticket[key] = 'paid'
                print(f"{key.title()} has been paid, you have 15 minutes to leave the garage")
    
    # Method that allows the user to leave the garage only if the value of the ticket is 'paid'
    def leaveGarage(self):
        while True:
            for value in self.current_ticket.values():
                if value == 'paid':
                    print("Thank you, have a nice day!")
                    self.tickets.append(15)
                    self.spaces.append(15)
                    break
                else:
                    print("If you don't pay, you may not leave the garage.")
                    my_garage.payForParking() # Asks them to pay again if they haven't already
            break







my_garage = ParkingGarage(tickets, parkingSpaces, current_ticket)
my_garage.takeTicket()
my_garage.payForParking()
my_garage.leaveGarage()
