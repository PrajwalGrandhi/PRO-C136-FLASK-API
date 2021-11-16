import csv

rows=[]

with open("final.csv", "r") as f:
  csvreader = csv.reader(f)
  for row in csvreader: 
    rows.append(row)

star_data_rows=rows[1:]

data=[]
for star_data in star_data_rows:
    temp_dict={
        'name':star_data[2],
        'constellation':star_data[3],
        'distance':star_data[4],
        'mass':star_data[5],
        'radius':star_data[6],
        'discovery':star_data[7],
        'gravity':star_data[8]
    }
    data.append(temp_dict)
    
print(data)