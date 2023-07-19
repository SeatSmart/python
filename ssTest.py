import math
from reportlab.pdfgen import canvas

dict1 = {'CSE': 2, 'ME': 1, 'ECE': 2, 'EEE': 0, 'CE': 0}
dict2 = {'CSE1': 120, 'CSE2': 93, 'ME1': 90, 'ECE1': 54, 'ECE2': 50}
dict3 = {'CSE1': [12, 23, 49, 32], 'CSE2': [39, 41], 'ME1': [11, 17], 'ECE1': [50], 'ECE2': []}
dict4 = {'CSE1': 'subject1', 'CSE2': 'subject1', 'ME1': 'subject2', 'ECE1': 'subject3', 'ECE2': 'subject3'}
dict5 = {'CSE1': 116, 'CSE2': 91, 'ME1': 88, 'ECE1': 53, 'ECE2': 50}
rm_lst = ['A301', 'A106', 'B202', 'B302', 'H216', 'H217']
h_lst = ['CB', 'MH']

dict5_sorted = dict(sorted(dict5.items(), key = lambda x:x[1], reverse = True))
print("dict5_sorted : ", dict5_sorted)
print()

'''total = 0
stdlst = list(dict5.values())
for i in range(len(stdlst)):
    total+=stdlst[i]

print(stdlst)
print(total)

T = total - hallcap
class_n = math.ceil(T/42)

print(class_n)'''

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

'''#allotin students
keys = list(dict_cl.keys())
clslst = list(dict_cl.values())

for m in range(len(clslst)):
    values = list(clslst[m].keys())
    print()
    print(values)
    print("Room:", keys[m])
    print()
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
                    print(j, "-", k1, allot[k1], end = '\t')
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
                    print(j, "-", k2, allot[k2],'\n')
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
                    print(j, "-", k1, allot[k1])
    except IndexError:
        print("Students are fully allotted")'''

output_file = "output.txt"

# Allotting students
keys = list(dict_cl.keys())
clslst = list(dict_cl.values())

with open(output_file, "w") as f:
    for m in range(len(clslst)):
        values = list(clslst[m].keys())
        room = keys[m]

        f.write(f"Room: {room}\n")
        
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
                        f.write(f"{j} - {k1}: {allot[k1]}\t")
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
                        f.write(f"{j} - {k1}: {allot[k1]}\n")      
        except IndexError:
            print("Students are fully allotted")


print("Output written to file:", output_file)


'''text_file = "output.txt"
pdf_file = "output.pdf"

# Read the content from the text file
with open(text_file, "r") as file:
    content = file.read()

# Create a new PDF file
c = canvas.Canvas(pdf_file)

# Set the font and font size
c.setFont("Helvetica", 12)

# Set the initial y-coordinate for drawing
y = 800
line_height = 15  # Adjust the line height as needed

# Write the content to the PDF
for line in content.split("\n"):
    c.drawString(50, y, line)
    y -= line_height

# Save and close the PDF file
c.save()

print("PDF file created:", pdf_file)'''

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

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
