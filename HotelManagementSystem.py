class HotelManagementSystem:
    def __init__(self, rt=0, s=0, p=0, r=0, t=0, a=1000, name='', address='', cindate='', coutdate='', rno=1):
        print("\n\n***HOTEL PACIFIC***\n")
        self.rt = rt
        self.r = r
        self.t = t
        self.p = p
        self.s = s
        self.a = a
        self.name = name
        self.address = address
        self.cindate = cindate
        self.coutdate = coutdate
        self.rno = rno

    # Customer Information
    def inputdata(self):
        self.name = input("\nEnter your Fullname: ")
        self.address = input("\nEnter your address: ")
        self.cindate = input("\nEnter your check-in date: ")
        self.coutdate = input("\nEnter your checkout date: ")
        print("Your room no.:", self.rno, "\n")

    # Room Rent
    def roomrent(self):
        print("We have the following rooms for you:-")
        print("1. Class A---->4000")
        print("2. Class B---->3000")
        print("3. Class C---->2000")
        print("4. Class D---->1000")

        x = int(input("Enter the number of your choice Please: "))
        n = int(input("For How Many Nights Did You Stay: "))

        if x == 1:
            print("You have chosen room Class A")
            self.s = 4000 * n
        elif x == 2:
            print("You have chosen room Class B")
            self.s = 3000 * n
        elif x == 3:
            print("You have chosen room Class C")
            self.s = 2000 * n
        elif x == 4:
            print("You have chosen room Class D")
            self.s = 1000 * n
        else:
            print("Please choose a valid room")
            self.s = 0

        print("Your chosen room rent is =", self.s, "\n")

    # Food Module
    def foodpurchased(self):
        print("*****RESTAURANT MENU*****")
        print("1. Dessert----->100")
        print("2. Drinks----->50")
        print("3. Breakfast--->90")
        print("4. Lunch---->110")
        print("5. Dinner--->150")
        print("6. Exit")

        while True:
            c = int(input("Enter the number of your choice: "))

            if c == 1:
                d = int(input("Enter the quantity: "))
                self.r += 100 * d
            elif c == 2:
                d = int(input("Enter the quantity: "))
                self.r += 50 * d
            elif c == 3:
                d = int(input("Enter the quantity: "))
                self.r += 90 * d
            elif c == 4:
                d = int(input("Enter the quantity: "))
                self.r += 110 * d
            elif c == 5:
                d = int(input("Enter the quantity: "))
                self.r += 150 * d
            elif c == 6:
                break
            else:
                print("You've Entered an Invalid Key")

        print("Total food Cost = Rs", self.r, "\n")

    # Billing Module
    def display(self):
        print("******HOTEL BILL******")
        print("Customer details:")
        print("Customer name:", self.name)
        print("Customer address:", self.address)
        print("Check-in date:", self.cindate)
        print("Check-out date:", self.coutdate)
        print("Room no.:", self.rno)
        print("Your Room rent is:", self.s)
        print("Your Food bill is:", self.r)

        self.rt = self.s + self.r

        print("Your subtotal Purchased is:", self.rt)
        print("Additional Service Charges is", self.a)
        print("Your grand total Purchased is:", self.rt + self.a, "\n")
        self.rno += 1

# Main Module of the System
def main():
    hotel = HotelManagementSystem()

    while True:
        print("1. Enter Customer Data")
        print("2. Calculate Room Rent")
        print("3. Calculate Food Purchased")
        print("4. Show Total Cost")
        print("5. EXIT")

        b = int(input("\nEnter the number of your choice: "))
        if b == 1:
            hotel.inputdata()
        elif b == 2:
            hotel.roomrent()
        elif b == 3:
            hotel.foodpurchased()
        elif b == 4:
            hotel.display()
        elif b == 5:
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
