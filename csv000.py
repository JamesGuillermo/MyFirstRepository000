import csv

""" with open('patients.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header
    writer.writerow(['ID Number', 'First Name', 'Middle Name', 'Last Name', 'Birthday', 'Gender'])
    # Write some example data

    writer.writerow(['x001', 'James', 'Guillermo', 'Cachero', '1999-12-16', 'Male']) """

with open('patients.csv', mode='r') as file:
    reader = csv.reader(file)

    # Print each row
    for row in reader:
        print(row)