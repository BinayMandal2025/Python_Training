class FlightNotFoundError(Exception):
    pass
class SeatsUnavailableError(Exception):
    pass
   
try:
    f = open('C:/RDT/Python/Data Types/Exception/flights.txt','r')

    try:
        data = f.read().split()
        fl_number, seats, price = data[0], int(data[1]), float(data[2])

        flightnumber = str(input("Enter flight number: "))
        
        if flightnumber != fl_number:
            raise FlightNotFoundError('Flight number does not exist!!!')
       
        reqticket = int(input("Enter number of ticket to book: "))
        if reqticket > seats:
          raise SeatsUnavailableError('Seats are not available!!!')
        
        totalcost = price * reqticket
        discount = (totalcost / reqticket) * 10 / 100
        print(f'Discounted total: {discount}')

        
    except ValueError:
        print("Please enter valid input")
    except ZeroDivisionError:
        print("Please enter valid seat number")
    
except FileNotFoundError:
    print('File not found, please check the path')
