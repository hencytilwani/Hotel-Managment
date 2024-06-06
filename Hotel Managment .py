from datetime import date

class Hotel:
    def __init__(self):
        self.rooms={}
        self.available_rooms={'std':[101,102,103],'Delux':[201,202,203],'Executive':[301,302,303],'Suite':[401,402,403]}
        self.roomprice={1:2000,2:4000,3:5000,4:6000}
        
    def check_in(self,name,address,phone):
        roomtype=int(input("Room Typees:\n1.Standard \n2.Delux \n3.Executive \n4.Suite \n select a room type"))
        if roomtype==1:
            if self.available_rooms['std']:
                room_no=self.available_rooms['std'].pop(0)
            else:
                print("Sorry,Standard Room Not Available")
                return
        elif roomtype==2:
            if self.available_rooms['Delux']:
                room_no=self.available_rooms['Delux'].pop(0)
            else:
                print("Sorry,delux Room Not Available")
                return
        elif roomtype==3:
            if self.available_rooms['Executive']:
                room_no=self.available_rooms['Executive'].pop(0)
            else:
                print("Sorry,Executive Room Not Available")
                return
        elif roomtype==4:
            if self.available_rooms['Suite']:
                room_no=self.available_rooms['Suite'].pop(0)
            else:
                print("Sorry,Suite Room Not Available")
                return
        else:
            print("Valid room type")
        d,m,y=map(int,input("Enter check-in-date in date,month,year").split())
        check_in=date(y,m,d)
        self.rooms[room_no]={
            'name':name,
            'address':address,
            'phone':phone,
            'check_in_date':check_in,
            'room_type':roomtype,
            'roomservice':0
        }
        print()
        print(f"checked in{name},{address} to room: {room_no} on {check_in}" )
        
    def room_service(self,room_no):
           if room_no in self.rooms:
                print()
                print("******* OYO Menu *******")
                print("1.Tea/Coffee: Rs.20 \n2.Desert: Rs.70 \n3.Breakfast: Rs:100 \n4. Lunch: Rs.150 \n5. Dinner: Rs.120 \n6.Exit")
                while 1:
                    c=int(input("Select your choice"))
                    if c==1:
                        q=int(input("Enter the Quantity: "))
                        self.rooms[room_no]['roomservice']+=20*q
                    elif c==2:
                        q=int(input("Enter the Quantity: "))
                        self.rooms[room_no]['roomservice']+=70*q
                    elif c==3:
                        q=int(input("Enter the Quantity: "))
                        self.rooms[room_no]['roomservice']+=100*q
                    elif c==4:
                        q=int(input("Enter the Quantity: "))
                        self.rooms[room_no]['roomservice']+=150*q
                    elif c==5:
                        q=int(input("Enter the Quantity: "))
                        self.rooms[room_no]['roomservice']+=120*q
                    elif c==6:
                        break
                    else:
                        print("invalid option")
                print("Room Services Rs: ",self.rooms[room_no]['roomservice'],"\n")
           else:
                print("Invalid room number")
    def display_occupied(self):
        if not self.rooms:
            print("No Rooms Are Occupied at the moment. ")
        else:
            print("Occupied Rooms")
            print("-------------------------------------------------------------")
            print('Room no.  Name   Phone')
            print("-------------------------------------------------------------")
            
            for room_number,details in self.rooms.items():
                print(room_number,'\t',details['name'],'\t',details['phone'])
   
    def generate_bill_and_checkout(self, room_number):
        if room_number in self.rooms:
            check_out_date = date.today()
            check_in_date = self.rooms[room_number]['check_in_date']
            duration = (check_out_date - check_in_date).days
            print("Duration of Stay:", duration, "days")
            room_type = self.rooms[room_number]['room_type']
            total_price = self.roomprice[room_type] * duration + self.rooms[room_number]['roomservice']
            bill_text = f"Bill for Room {room_number}:\nRoom Price: {self.roomprice[room_type]} * {duration} days = {self.roomprice[room_type] * duration}\nRoom Service Charges: {self.rooms[room_number]['roomservice']}\nTotal: {total_price}"
            with open(f"bill_room_{room_number}.txt", 'w') as bill_file:
                bill_file.write(bill_text)
            print("Bill generated successfully.")
            del self.rooms[room_number]
        else:
            print("Invalid room number")
    def search_record(self):
            search_term = input("Enter guest name or phone number to search: ")
            found = False
            for room_number, details in self.rooms.items():
                if search_term.lower() in details['name'].lower() or search_term in details['phone']:
                    print("Guest found in Room:", room_number)
                    print("Name:", details['name'])
                    print("Address:", details['address'])
                    print("Phone:", details['phone'])
                    found = True
            if not found:
                print("No guest found with the provided search term.")

        
    def update_record(self):
        room_number = int(input("Enter Room Number to update record: "))
        if room_number in self.rooms:
            details = self.rooms[room_number]
            print("Current Details:")
            print("Name:", details['name'])
            print("Address:", details['address'])
            print("Phone:", details['phone'])
            choice = input("What do you want to update? (name/address/phone): ").lower()
            if choice == 'name':
                details['name'] = input("Enter new name: ")
            elif choice == 'address':
                details['address'] = input("Enter new address: ")
            elif choice == 'phone':
                details['phone'] = input("Enter new phone number: ")
            else:
                print("Invalid choice.")
        else:
            print("Invalid room number.")

    
    def start_app(self):
        while True:
            print("-------------------------------------------------------------")
            print()
            print("Welcome to Taj Hotel")
            print()
            print("1. check-in")
            print("2. Room Service")
            print("3. Display occupied room")
            print("4. Generate Bill and checkout")
            print("5. Search Record ")
            print("6. update Record ")
            print("7. exit")
            print()
            print("-------------------------------------------------------------")
            choice=input("Enter your choice:")
            if choice=='1':
                name=input("Enter Name")
                Address=input("Enter Address: ")
                phone=input("Enter contact number")
                self.check_in(name,Address,phone)
                
            elif choice=='2':
                room_no=int(input("Enter Room Number"))
                self.room_service(room_no)
                
            elif choice=='3':
                self.display_occupied()
                
            elif choice=='4':
                room_number=int(input("Enter Room Number"))
                self.generate_bill_and_checkout(room_number)
                
            elif choice=='5':
                self.search_record()
            
            elif choice=='6':
                self.update_record()
            
            elif choice=='7':
                break
                
            else:
                print("Invalid choice. Please Try Again")
                
h=Hotel()
h.start_app()