import csv

data = []
with open("bright_stars.csv","r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data.append(row)

headers = data[0]
star_data = data[1:]

# converting all data names to lower case
for data_point in star_data:
    data_point[2] = data_point[2].lower()

# sorting star names in alphabetical order
star_data.sort(key=lambda star_data: star_data[2])

# sorting is done. writing a new csv file
with open ("data2_sorted.csv","a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerow(star_data)
