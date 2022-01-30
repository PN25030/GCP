import csv
# read a pre-existing file
file = open('test.csv')
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
rows = []
rows1 = []
for row in csvreader:
    rows.append(row)
    print(row, end='\n')

#write this data to new file
target_file_name = 'new_test.csv'
with open(target_file_name,'w') as file1:
    for row in rows:
        file1.write(str(row))
        file1.write('n')
file.close()
file1.close()