import math
import json
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

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

dict5_sorted = dict(sorted(dict5.items(), key = lambda x:x[1], reverse = True))
print("dict5_sorted : ", dict5_sorted)
print()

#capacity of halls
cb_cap = 170
ch_cap = 62
mh_cap = 120

cb = 0
ch = 0
mh = 0

#lists to store classes
lst_cblock = []
lst_chall = []
lst_mhall = []

#alloted hall dictionaries
dict_cb = {}
dict_ch = {}
dict_mh = {}

#allotting classes to halls
if ('CB' in h_lst):
    for i in dict5_sorted:
        cb += dict5_sorted[i]
        if (cb <= 170):
            lst_cblock.append(i)
            dict_cb[i] = dict5_sorted[i]
            cb_cap -= dict5_sorted[i]
        else:
            cb -= dict5_sorted[i]

print("cblock alloted : ", lst_cblock)
dict6 = dict5_sorted
for i in range(len(lst_cblock)):
    if (lst_cblock[i] in dict6):
        del dict6[lst_cblock[i]]


if ('CH' in h_lst):
    for i in dict6:
        ch += dict6[i]
        if (ch <= 62):
            lst_chall.append(i)
            dict_ch[i] = dict6[i]
            ch_cap -= dict6[i]
        else:
            ch -= dict6[i]


for i in range(len(lst_chall)):
    if (lst_chall[i] in dict6):
        del dict6[lst_chall[i]]

print("civil hall alloted : ", lst_chall)

if ('MH' in h_lst):
    for i in dict6:
        mh += dict6[i]
        if (mh <= 110):
            lst_mhall.append(i)
            dict_mh[i] = dict6[i]
            mh_cap -= dict6[i]
        else:
            mh -= dict6[i]

for i in range(len(lst_mhall)):
    if (lst_mhall[i] in dict6):
        del dict6[lst_mhall[i]]

print("mech hall alloted : ", lst_mhall)
print()
print("dict6 : ", dict6)
print()

print("capacity of cblcok : ", cb_cap)
print("capacity of civil hall : ", ch_cap)
print("capacity of mech hall : ", mh_cap)
print()

for i in dict6:
    if ('CB' in h_lst):
        class_half = math.ceil(dict6[i]/2)
        if (cb_cap > class_half):
            dict6[i] -= class_half
            dict_cb[i] = class_half
            cb_cap -= class_half
            continue
    if ('CH' in h_lst):
        class_half = math.ceil(dict6[i]/2)
        if (ch_cap > class_half):
            dict6[i] -= class_half
            dict_ch[i] = class_half
            ch_cap -= class_half
            continue
    if ('MH' in h_lst):
        class_half = math.ceil(dict6[i]/2)
        if (mh_cap > class_half):
            dict6[i] -= class_half
            dict_mh[i] = class_half
            mh_cap -= class_half
            continue

#class strength - 21 < threshold value (12), allot them too

#pb1 - more classes in exam halls give problem??
#pb2 - half the class strength in remaining capacity

print("cblock alloted students : ", dict_cb)
print()
print("civil hall alloted students : ", dict_ch)
print()
print("mech hall alloted students : ", dict_mh)
print()
print("dict 6 after alloting : ", dict6)
print()
print(cb_cap)
print(ch_cap)
print(mh_cap)


#alloting classes to classrooms

dict_cl = {}    #class_id mapped to class

print(rm_lst)
print(dict6)
dict6_key = list(dict6.keys())
print(dict6_key)

for i in rm_lst:
    dict_class = {}
    strength = 0
    for j in dict6:
        if (dict6[j] <= 0):
            continue
        else:
            if (strength < 42):
                if (dict6[j] >= 21):
                    dict_class[j] = 21
                    dict6[j] -= 21
                    strength += 21
                else:
                    dict_class[j] = dict6[j]
                    dict6[j] -= dict6[j]
                    strength += 21
    dict_cl[i] = dict_class
    templst = list(dict_class.keys())
    print(templst)
    if (len(templst)==2):
        if (dict4[templst[0]] == dict4[templst[1]]):
            dict6[templst[1]] += dict_class[templst[1]]
            del dict_class[templst[1]]
        
    
        
print(dict_cl)
print(dict6)


allot = {}

output_file = "output.txt"

# Allotting students
keys = list(dict_cl.keys())
clslst = list(dict_cl.values())

with open(output_file, "w") as f:
    for m in range(len(clslst)):
        values = list(clslst[m].keys())
        room = keys[m]

        f.write(f"\n\nRoom: {room}\n")
        
        try:
            if len(values) == 2:
                k1 = values[0]
                k2 = values[1]
                for j in range(1, 43):
                    if j % 2 != 0:
                        if k1 in allot:
                            if allot[k1] + 1 <= dict2[k1] and allot[k1] + 1 not in dict3[k1]:
                                allot[k1] += 1
                            elif allot[k1] + 1 <= dict2[k1] and allot[k1] + 1 in dict3[k1]:
                                allot[k1] += 2
                            elif allot[k1] + 1 > dict2[k1]:
                                continue
                        else:
                            if 1 not in dict3[k1]:
                                allot[k1] = 1
                            else:
                                allot[k1] = 2
                        f.write(f"\n{j} - {k1}: {allot[k1]}\t")
                    else:
                        if k2 in allot:
                            if allot[k2] + 1 <= dict2[k2] and allot[k2] + 1 not in dict3[k2]:
                                allot[k2] += 1
                            elif allot[k2] + 1 <= dict2[k2] and allot[k2] + 1 in dict3[k2]:
                                allot[k2] += 2
                            elif allot[k2] + 1 > dict2[k2]:
                                continue
                        else:
                            if 1 not in dict3[k2]:
                                allot[k2] = 1
                            else:
                                allot[k2] = 2
                        f.write(f"{j} - {k2}: {allot[k2]}\n")
            else:
                k1 = values[0]
                for j in range(1, 43):
                    if j % 2 != 0:
                        if k1 in allot:
                            if allot[k1] + 1 <= dict2[k1] and allot[k1] + 1 not in dict3[k1]:
                                allot[k1] += 1
                            elif allot[k1] + 1 <= dict2[k1] and allot[k1] + 1 in dict3[k1]:
                                allot[k1] += 2
                            elif allot[k1] + 1 > dict2[k1]:
                                continue
                        else:
                            if 1 not in dict3[k1]:
                                allot[k1] = 1
                            else:
                                allot[k1] = 2
                        f.write(f"\n{j} - {k1}: {allot[k1]}\n")      
        except IndexError:
            print("Students are fully allotted")


print("Output written to file:", output_file)


text_file = "output.txt"
pdf_file = "output.pdf"

# Read the content from the text file
with open(text_file, "r") as file:
    content = file.readlines()

# Create a new PDF file
c = canvas.Canvas(pdf_file, pagesize=letter)

# Set the font and font size
c.setFont("Helvetica", 12)

# Set the initial y-coordinate for drawing
y = 10 * inch  # Start from the top of the page
line_height = 15  # Adjust the line height as needed

# Iterate through the content lines
for line in content:
    line = line.strip()

    # Check if the remaining space is enough for the next line
    if y < 0.75 * inch:  # Adjust the threshold as needed
        c.showPage()  # Add a new page
        y = 10 * inch  # Reset the y-coordinate for the new page

    # Replace tab characters with spaces
    line = line.replace('\t', ' ' * 8)  # Assuming 8 spaces per tab

    # Write the line to the PDF
    c.drawString(1 * inch, y, line)

    # Update the y-coordinate for the next line
    y -= line_height

# Save and close the PDF file
c.save()

print("PDF file created:", pdf_file)

