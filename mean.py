import csv

with open('SOCR-HeightWeight.csv', newline='')as f:
     reader = csv.reader(f)
     data = list(reader)
     

data.pop(0)

new_data = []

for i in range(len(data)):
     n_num = data[i][2]
     new_data.append(float(n_num))
     
n = len(new_data)
total = 0

for x in new_data:
     total += x
     
mean = total/n
print("mean is : "+ str(mean))
