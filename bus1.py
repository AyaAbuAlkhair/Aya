
class bus1:
    def seats():
        print("[1]__[2]__[3]__[4]__[5]__[6]__[7]__[8]__[9]__[10]")
        print("[11]_[12]_[13]_[14]_[15]_[16]_[17]_[18]_[19]_[20]")

        seatNoList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        while(True):
            seatNo = int(input("choose your seat number: "))

            if seatNo in seatNoList:
                   name = (input("your name: "))
                   print("the seat is reserved for you", name)
                   seatNoList[seatNo-1]="R"
                   print(seatNoList)
            else:
                   print("This seat is already reserved! try another one")

            print("Do you wanna try another bus?")
            q=input("your answer yes/no: ")
            if q=="yes":
                menu()
            else:
                continue
                print(seatNoList)
            break
class bus2:
    def seats2():
        print("1,2,3,4,5,6,7,8,9,10,11,12,13,14")
        print("15,16,17,18,19,20,21,22,23,24,25")

        seat2NoList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,21,22,23,24,25]
        while(True):
            seat2No = int(input("choose your seat number: "))

            if seat2No in seat2NoList:
                   name = (input("your name: "))
                   print("the seat is reserved for you", name)
                   seat2NoList[seat2No-1]="R"
                   print(seat2NoList)
            else:
                   print("This seat is already reserved! try another one")

            print("Do you wanna try another bus?")
            q=input("your answer yes/no: ")
            if q=="yes":
                menu()
            else:
                continue
                print(seat2NoList)
            break
obj1=bus1
obj2=bus2

def menu():
    print("1. bus1 from Gaza to Jerusalem")
    print("2. bus2 from Gaza to Ramallah")
    global ch
    ch = int(input("Choose your bus: "))

while(True):
    menu()
    if ch == 1:
        obj1.seats()
    elif ch==2:
        obj2.seats2()

obj1.seats
obj2.seats2