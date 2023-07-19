import math
import json
import random

dict1 = {}  #branches
dict2 = {}  #rollnumberRange
vac_lst = []    #vacant roll list
dict3 = {}  #class - vacant roll dictionary
dict4 = {}  #course
dict5 = {}  #total students
rm_lst = [] #room list
h_lst = []  #hall list
cblock =  170  #capacity
mech_hall = 110
civil_hall = 62
hallcap = 0

while True:
    print("1 : Exam cell")
    print("2 : Invigilator")
    print("3 : Exit")
    ch = int(input("Choose your option : "))
    if (ch == 1):
        print("1 : Internal")
        print("2 : External")
        print("3 : Go back")
        ch == int(input("Choose your option : "))
        if (ch == 1):
            while True:     #Choosing branches and number of classes for each
                print("1 : CSE")
                print("2 : EEE")
                print("3 : ECE")
                print("4 : CE")
                print("5 : ME")
                print("6 : Exit/Confirm")
                ch2 = int(input("Choose branch : "))
                if (ch2 == 1):  #and ("CSE" not in dict1)
                    if ("CSE" in dict1):
                        print("You have already entered the classes.")
                        ch3 = input("Do you want to overwrite? (y/n)")
                        if (ch3 == 'y'):
                            del dict1["CSE"]
                            n = int(input("Enter the number of classes : "))
                            dict1["CSE"] = n
                        elif (ch3 == 'n'):
                            continue
                        else:
                            print("Invalid option")
                    else:
                        n = int(input("Enter the number of classes : "))
                        dict1["CSE"] = n
                elif (ch2 == 2):
                    if ("EEE" in dict1):
                        print("You have already entered the classes.")
                        ch3 = input("Do you want to overwrite? (y/n)")
                        if (ch3 == 'y'):
                            del dict1["EEE"]
                            n = int(input("Enter the number of classes : "))
                            dict1["EEE"] = n
                        elif (ch3 == 'n'):
                            continue
                        else:
                            print("Invalid option")
                    else:
                        n = int(input("Enter the number of classes : "))
                        dict1["EEE"] = n
                elif (ch2 == 3):
                    if ("ECE" in dict1):
                        print("You have already entered the classes.")
                        ch3 = input("Do you want to overwrite? (y/n)")
                        if (ch3 == 'y'):
                            del dict1["ECE"]
                            n = int(input("Enter the number of classes : "))
                            dict1["ECE"] = n
                        elif (ch3 == 'n'):
                            continue
                        else:
                            print("Invalid option")
                    else:
                        n = int(input("Enter the number of classes : "))
                        dict1["ECE"] = n
                elif (ch2 == 4):
                    if ("CE" in dict1):
                        print("You have already entered the classes.")
                        ch3 = input("Do you want to overwrite? (y/n)")
                        if (ch3 == 'y'):
                            del dict1["CE"]
                            n = int(input("Enter the number of classes : "))
                            dict1["CE"] = n
                        elif (ch3 == 'n'):
                            continue
                        else:
                            print("Invalid option")
                    else:
                        n = int(input("Enter the number of classes : "))
                        dict1["CE"] = n
                elif (ch2 == 5):
                    if ("ME" in dict1):
                        print("You have already entered the classes.")
                        ch3 = input("Do you want to overwrite? (y/n)")
                        if (ch3 == 'y'):
                            del dict1["ME"]
                            n = int(input("Enter the number of classes : "))
                            dict1["ME"] = n
                        elif (ch3 == 'n'):
                            continue
                        else:
                            print("Invalid option")
                    else:
                        n = int(input("Enter the number of classes : "))
                        dict1["ME"] = n
                elif (ch2 == 6):
                    break
                else:
                    print("Invalid number")
            for i in ["CSE","EEE","ECE","CE","ME"]:
                if (i not in dict1):
                    dict1[i] = 0

            print(dict1)
            print(dict2)
            lst0_k = list(dict1.keys())   #Roll range, vacant roll, and total students for each class
            lst0_v = list(dict1.values())
            for i in range(len(lst0_k)):
                if (lst0_v[i] != 0):
                    for j in range(1,lst0_v[i]+1):
                        print(lst0_k[i]+str(j))
                        vac_lst = []
                        roll = int(input("Enter the last roll number (for range) : "))
                        dict2[lst0_k[i]+str(j)] = roll
                        vac_n = int(input("Enter the number of vacant students : "))
                        for k in range(vac_n):
                            vn = int(input("Enter vacant roll (if none, enter zero): "))
                            while True:
                                if (vn > roll):
                                    print("Invalid roll number")
                                    vn = int(input("Enter vacant roll (if none, enter zero): "))
                                else:
                                    break
                            vac_lst.append(vn)
                        if (vac_lst == []):
                            dict3[lst0_k[i]+str(j)] = []  #continue
                        else:
                            dict3[lst0_k[i]+str(j)] = vac_lst
                        course = input("Enter the course : ")
                        dict4[lst0_k[i]+str(j)] = course
                        total = roll - vac_n
                        dict5[lst0_k[i]+str(j)] = total

            #Rooms
            rn = int(input("Enter the number of classrooms available : "))
            for i in range(rn):
                room = input("Enter the room id (eg:- A301) : ")
                rm_lst.append(room)

            #Halls
            h1 = input("C block hall available? (y/n) :")
            h2 = input("Civil hall available? (y/n) :")
            h3 = input("Mech hall available? (y/n) :")
            if (h1 == 'y'):
                h_lst.append("CB")
                hallcap+=cblock
            if (h2 == 'y'):
                h_lst.append("CH")
                hallcap+=civil_hall
            if (h3 == 'y'):
                h_lst.append("MH")
                hallcap+=mech_hall

            print(dict1)
            print(dict2)
            print(dict3)
            print(dict4)
            print(dict5)
            print(rm_lst)
            print(h_lst)
        elif (ch == 2):
            continue
        elif (ch == 3):
            break
        else:
            print("Invalid number")
    elif (ch == 2):
        continue
    elif (ch == 3):
        break
    else:
        print("Invalid number")
            
#seating arrangement

total = 0
stdlst = list(dict5.values())
for i in range(len(stdlst)):
    total+=stdlst[i]

print(stdlst)
print(total)

T = total - hallcap
class_n = math.ceil(T/42)

print(class_n)

ran_index = random.randint(0, len(dict5))


