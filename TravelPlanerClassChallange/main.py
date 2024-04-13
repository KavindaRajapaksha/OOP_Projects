class Travel_Planner:
     def __init__(self,country,month,type):
        self.country = country
        self.month = int(month)
        self.type = type
        self.price = 0
    
     def trip_info(self):
        if self.month>=10 and self.month<=3:
           print(f"You are going to {self.country} in the winter! and this is a {self.type} trip")
        elif self.month>=4 and self.month<=10:
           print(f"You are going to {self.country} in the spring! and this is a {self.type} trip")
        else:
           print("Invalid month")

     def cal_cost(self,cost):
        costs=[]
        while cost!=0:
           self.price+=cost
           costs.append(cost)
           cost = int(input("Enter the cost of the next item: "))

      
        advice=self.advice(self.price)
        inspect=self.list_inspect(costs)
        return advice,inspect
        #call next method 
        #call checker method
        #return two things

     def advice(self,num):
        if num<500 :
              print("low budget!")
        elif num>=500 and num<=1500:
              print("medium budget!")
        elif num>1500:
                print("high budget!")
        else:
                print("Luxury budget")

     def list_inspect(self,costs):
        less_than_ten=0
        for i in costs:
            if i>= 10:
                less_than_ten+=1

        if less_than_ten<=10:
            self.price+=100
            print(f'Updated price: {self.price}')

location = input("Enter the country you are going to: ").capitalize()
month = int(input("Enter the month you are going to: "))
type = input("Enter the type of the trip: ")

trip = Travel_Planner(location,month,type)
trip.trip_info()
flight_cost = int(input("Enter the cost of the flight: "))
trip.cal_cost(flight_cost)




# trip.cal_cost(cost)

# test = Travel_Planner("USA", 5, "Business")
# test.trip_info()

# test.cal_cost(100)

    
            

   