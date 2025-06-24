import csv

class PatientDetails:
    def __init__(self, firstName, middleName, lastName, birthDate, gender ):
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        self.birthDate = birthDate
        self.gender = gender

    def showDetails(self):
        print("First Name:", self.firstName)
        print("Middle Name:", self.middleName)
        print("Last Name:", self.lastName)
        print("Birth Date:", self.birthDate)
        print("Gender:", self.gender)

with open('patients.csv', mode='r') as file:
    reader = csv.reader(file)
    data = list(reader)  # Now it's a list of rows

with open('patients.csv', mode='a', newline='') as file:
    writer = csv.writer(file)

while True:
    print("1. Register New Patient")
    print("2. Show Patient Details")
    print("3. Exit")

    choice = input("Enter your choice: ")  

    if choice == "1":
        firstName = input("Enter First Name: ")
        middleName = input("Enter Middle Name: ")
        lastName = input("Enter Last Name: ")
        birthDate = input("Enter Birth Date (YYYY-MM-DD): ")
        gender = input("Gender: ")

        idNumber = input("Enter ID Number: ")

        with open('patients.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([idNumber, firstName, middleName, lastName, birthDate, gender])
        
        print("Patient registered successfully!")
    elif choice == "2": 
        print("Patient Details:")

        inputIdNumber = input("Enter ID Number to show details: ")

        for i in range(1, len(data)):
            if inputIdNumber == data[i][0]: # Check if the first column matches the input
                 #print(f"Patient found: {data[i]}")
                for value in data[i]:
                    print(value, end=' ')
                break
            elif i == len(data) - 1:
                print("Patient not found.")
        
    elif choice == "3":
        print("Exiting the program.")
        break