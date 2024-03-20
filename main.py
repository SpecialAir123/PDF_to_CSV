import csv
import re
import numpy as np
import pandas as pd
import sys

# with open('Archived_Certifications.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile, delimiter=' ')
#     for i in range(5):
#         row = next(reader)
#         print(row)

file = open("Archived_Certifications.csv")

for i in range(4):
    row = next(file)
category = row.split()
category[0] = category[0].replace('"','')
category[-1] = category[-1].replace('"','')
category.pop(8)
category[7] = category[7] + ' #'
category[4] = category[4]+" "+category[5]
category.pop(5)
category[2] = category[2]+" "+category[3]
category.pop(3)


print(category)
print(len(category))
input = []
for i in range(len(category)):
    input.append("")


row = next(file)
row = next(file)
row = next(file)
row = next(file)

print(row)
# result = re.search(r'\b.*?\.', row)
# row = re.sub(r'\b.*?\.','', row)
# print(result.group())


# input[0] = result.group()
row = row.replace('"','')
row = row.split()
print(row)
input[0] = ' '.join(row[:-4])
input[1] = row[-4]
input[3] = row[-3]
input[4] = row[-2]
input[6] = row[-1]

print("input is", input)






df = pd.DataFrame(category)
df = df.T
df.loc[len(df)] = input

for line in file:
    if "Valid" in line:
        row = line
        row = row.replace('"', '')
        row = row.split()

        if row[-1] == "Valid":
            input[0] = ' '.join(row[:-3])
            input[1] = row[-3]
            input[3] = row[-2]
            input[4] = row[-1]
            input[6] = ""
        else:
            input[0] = ' '.join(row[:-4])
            input[1] = row[-4]
            input[3] = row[-3]
            input[4] = row[-2]
            input[6] = row[-1]




        print("input is", input)
        df.loc[len(df)] = input

print(df)
df.to_csv('file1.csv')