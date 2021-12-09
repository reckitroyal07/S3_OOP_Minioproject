import datetime
import unittest
from datetime import datetime,timedelta
class BikeRental:
    
    def __init__(self,stock=0):
        """
        Our constructor class that instantiates bike rental shop.
        """
        self.stock = stock 
    def displaystock(self):
        """
        Displays the bikes currently available for rent in the shop.
        """
        print("We have currently {} bikes available to     rent.".format(self.stock))
        return self.stock
    def rentBikeOnHourlyBasis(self, n):
        """
        Rents a bike on hourly basis to a customer.
        """
        # reject invalid input 
        if n <= 0:
            print("Number of bikes should be positive!")
            return None
        # do not rent bike is stock is less than requested bikes
        
        elif n > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None
        # rent the bikes        
        else:
            now = datetime.datetime.now()                      
            print("You have rented a {} bike(s) on hourly basis today at {} hours.".format(n,now.hour))
            print("You will be charged $5 for each hour per bike.")
            print("We hope that you enjoy our service.")
            self.stock -= n
            return now      
     
    def rentBikeOnDailyBasis(self, n):
        """
        Rents a bike on daily basis to a customer.
        """
        
        if n <= 0:
            print("Number of bikes should be positive!")
            return None
        elif n > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None
    
        else:
            now = datetime.datetime.now()                      
            print("You have rented {} bike(s) on daily basis today at {} hours.".format(n, now.hour))
            print("You will be charged $20 for each day per bike.")
            print("We hope that you enjoy our service.")
            self.stock -= n
            return now
        
    def rentBikeOnWeeklyBasis(self, n):
        """
        Rents a bike on weekly basis to a customer.
        """
        if n <= 0:
            print("Number of bikes should be positive!")
            return None
        elif n > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None        
        
        else:
            now = datetime.datetime.now()
            print("You have rented {} bike(s) on weekly basis today at {} hours.".format(n, now.hour))
            print("You will be charged $60 for each week per bike.")
            print("We hope that you enjoy our service.")
            self.stock -= n
            return now
    
    
    def returnBike(self, request):
        """
        1. Accept a rented bike from a customer
        2. Replensihes the inventory
        3. Return a bill
        """
       
        # extract the tuple and initiate bill
        rentalTime, rentalBasis, numOfBikes = request
        bill = 0
        # issue a bill only if all three parameters are not null!
        if rentalTime and rentalBasis and numOfBikes:
            self.stock += numOfBikes
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime
        
            # hourly bill calculation
            if rentalBasis == 1:
                bill = round(rentalPeriod.seconds / 3600) * 5 * numOfBikes
                
            # daily bill calculation
            elif rentalBasis == 2:
                bill = round(rentalPeriod.days) * 20 * numOfBikes
                
            # weekly bill calculation
            elif rentalBasis == 3:
                bill = round(rentalPeriod.days / 7) * 60 * numOfBikes
            
            # family discount calculation
            if (3 <= numOfBikes <= 5):
                print("You are eligible for Family rental promotion of 30% discount")
                bill = bill * 0.7
            print("Thanks for returning your bike. Hope you enjoyed our service!")
            print("That would be ${}".format(bill))
            return bill
        
        else:
            print("Are you sure you rented a bike with us?")
            return None


class Customer:
    def __init__(self):
        """
        Our constructor method which instantiates various customer objects.
        """
        
        self.bikes = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0
    
    def requestBike(self):
        """
        Takes a request from the customer for the number of bikes.
        """
                      
        bikes = input("How many bikes would you like to rent?")
        
        # implement logic for invalid input
        try:
            bikes = int(bikes)
        except ValueError:
            print("That's not a positive integer!")
            return -1
        if bikes < 1:
            print("Invalid input. Number of bikes should be greater than zero!")
            return -1
        else:
            self.bikes = bikes
        return self.bikes
     
    def returnBike(self):
        """
        Allows customers to return their bikes to the rental shop.
        """
        if self.rentalBasis and self.rentalTime and self.bikes:
            return self.rentalTime, self.rentalBasis, self.bikes  
        else:
            return 0,0,0

class BikeRentalTest(unittest.TestCase):
    def test_Bike_Rental_diplays_correct_stock(self):
        shop1 = BikeRental()
        shop2 = BikeRental(10)
        self.assertEqual(shop1.displaystock(), 0)
        self.assertEqual(shop2.displaystock(), 10)
        
    def test_rentBikeOnHourlyBasis_for_negative_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnHourlyBasis(-1), None)
    def test_rentBikeOnHourlyBasis_for_zero_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnHourlyBasis(0), None)
    def test_rentBikeOnHourlyBasis_for_valid_positive_number_of_bikes(self):
        shop = BikeRental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.rentBikeOnHourlyBasis(2).hour, hour)
    def test_rentBikeOnHourlyBasis_for_invalid_positive_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnHourlyBasis(11), None)
    def test_rentBikeOnDailyBasis_for_negative_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnDailyBasis(-1), None)
    def test_rentBikeOnDailyBasis_for_zero_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnDailyBasis(0), None)
    def test_rentBikeOnDailyBasis_for_valid_positive_number_of_bikes(self):
        shop = BikeRental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.rentBikeOnDailyBasis(2).hour, hour)
    def test_rentBikeOnDailyBasis_for_invalid_positive_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnDailyBasis(11), None)
     
    def test_rentBikeOnWeeklyBasis_for_negative_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnWeeklyBasis(-1), None)
    def test_rentBikeOnWeeklyBasis_for_zero_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnWeeklyBasis(0), None)
    def test_rentBikeOnWeeklyBasis_for_valid_positive_number_of_bikes(self):
        shop = BikeRental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.rentBikeOnWeeklyBasis(2).hour, hour)
    def test_rentBikeOnWeeklyBasis_for_invalid_positive_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnWeeklyBasis(11), None)
    
    def test_returnBike_for_invalid_rentalTime(self):
        # create a shop and a customer
        shop = BikeRental(10)
        customer = Customer()
        # let the customer not rent a bike a try to return one.
        request = customer.returnBike()
        self.assertIsNone(shop.returnBike(request))
        # manually check return function with error values
        self.assertIsNone(shop.returnBike((0,0,0)))
        
    def test_returnBike_for_invalid_rentalBasis(self):
        # create a shop and a customer
        shop = BikeRental(10)
        customer = Customer()
        
        # create valid rentalTime and bikes
        customer.rentalTime = datetime.now()
        customer.bikes = 3
        # create invalid rentalbasis
        customer.rentalBasis = 7
        request = customer.returnBike()
        self.assertEqual(shop.returnBike(request), 0)
    def test_returnBike_for_invalid_numOfBikes(self):
     
        # create a shop and a customer
        shop = BikeRental(10)
        customer = Customer()
        
        # create valid rentalTime and rentalBasis
        customer.rentalTime = datetime.now()
        customer.rentalBasis = 1
        # create invalid bikes
        customer.bikes = 0
        request = customer.returnBike()
        self.assertIsNone(shop.returnBike(request))
    def test_returnBike_for_valid_credentials(self):
     
        # create a shop and a various customers
        shop = BikeRental(50)
        customer1 = Customer()
        customer2 = Customer()
        customer3 = Customer()
        customer4 = Customer()
        customer5 = Customer()
        customer6 = Customer()
        
        # create valid rentalBasis for each customer
        customer1.rentalBasis = 1 # hourly
        customer2.rentalBasis = 1 # hourly
        customer3.rentalBasis = 2 # daily
        customer4.rentalBasis = 2 # daily
        customer5.rentalBasis = 3 # weekly
        customer6.rentalBasis = 3 # weekly
        # create valid bikes for each customer
        customer1.bikes = 1
        customer2.bikes = 5 # eligible for family discount 30%
        customer3.bikes = 2
        customer4.bikes = 8 
        customer5.bikes = 15
        customer6.bikes = 30
        # create past valid rental times for each customer
        
        customer1.rentalTime = datetime.now() + timedelta(hours=-4)
        customer2.rentalTime = datetime.now() + timedelta(hours=-23)
        customer3.rentalTime = datetime.now() + timedelta(days=-4)
        customer4.rentalTime = datetime.now() + timedelta(days=-13)
        customer5.rentalTime = datetime.now() + timedelta(weeks=-6)
        customer6.rentalTime = datetime.now() + timedelta(weeks=-12)
        # make all customers return their bikes
        request1 = customer1.returnBike()
        request2 = customer2.returnBike()
        request3 = customer3.returnBike()
        request4 = customer4.returnBike()
        request5 = customer5.returnBike()
        request6 = customer6.returnBike()
        # check if all of them get correct bill
        self.assertEqual(shop.returnBike(request1), 20)
        self.assertEqual(shop.returnBike(request2), 402.5)
        self.assertEqual(shop.returnBike(request3), 160)
        self.assertEqual(shop.returnBike(request4), 2080)
        self.assertEqual(shop.returnBike(request5), 5400)
        self.assertEqual(shop.returnBike(request6), 21600)

class CustomerTest(unittest.TestCase):
    
    def test_return_Bike_with_valid_input(self):
        # create a customer
        customer = Customer()
        
        # create valid rentalTime, rentalBasis, bikes
        now = datetime.now()
        customer.rentalTime = now
        customer.rentalBasis = 1
        customer.bikes = 4
        self.assertEqual(customer.returnBike(),(now,1, 4))
    def test_return_Bike_with_invalid_input(self):
        # create a customer
        customer = Customer()
        
        # create valid rentalBasis and bikes
               
        customer.rentalBasis = 1
        customer.bikes = 0
        # create invalid rentalTime
        customer.rentalTime =  0
        self.assertEqual(customer.returnBike(),(0,0,0))
if __name__ == '__main__':
    unittest.main()