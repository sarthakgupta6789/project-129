import csv
import pandas as pd

file1 = 'data2_sorted.csv'
file2 = 'dwarf_stars.csv'

dataset1 = []
dataset2 = []
with open("data2_sorted.csv",'r') as f:
    csv_reader =csv.reader(f)
    
    for i in csv_reader:
        dataset1.append(i)
        
with open("dwarf_stars.csv",'r') as f:
    csv_reader = csv.reader(f)
    
    for i in csv_reader:
        dataset2.append(i)

headers1 = dataset1[0]
headers2 = dataset2[0]

starsdataset1 = dataset1[1:]
starsdataset2 = dataset2[1:]

h = headers1+headers2

starsd =[]

for i in starsdataset1:
    starsd.append(i)
for j in starsdataset2:
    starsd.append(j)

with open("total_stars.csv",'w') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)   
    csvwriter.writerows(starsd)
    
df = pd.read_csv('total_stars.csv')
