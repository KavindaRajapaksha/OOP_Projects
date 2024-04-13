class Guest:
    def __init__(self,last,first,rank,age):
        self.last_name = last
        self.first_name = first
        self.rank = int(rank)
        self.age = age
    
    def guest_info(self,all_guests):
        for guest in all_guests:
           print(f"Guest: {guest.first_name} {guest.last_name} is {guest.age} years old and is a rank {guest.rank} member")

    def loyalty_programme(self,all_guests):
       
       gold_members=[self.last_name for guest in all_guests if guest.rank>=10]
       if gold_members:
           print("Gold members:")
           for member in gold_members:
            print("Guest:",member)
    def guess_avg(self,all_guests):
       total_age=0
       for guest in all_guests:
           total_age+=guest.age
       average_age=total_age/len(all_guests)
       print(f"Average age of guests: {average_age}")


all_guests=list()
num_guests=int(input("Enter the number of guests: "))   
for i in range(num_guests):
    data=input("Enter the last name, first name, rank , age of the guest: ").split(",")
    guest=Guest(data[0],data[1],data[2],data[3])
    all_guests.append(guest)

guest=all_guests[0]
guest.guest_info(all_guests)
guest.loyalty_programme(all_guests)
guest.guess_avg(all_guests)