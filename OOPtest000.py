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

patientsData = {}

f = open("ReadMe.txt")
print(f.read())
f.close()

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

        patientsData[idNumber] = PatientDetails(firstName, middleName, lastName, birthDate, gender)
        
        print("Patient registered successfully!")
    elif choice == "2": 
        print("Patient Details:")

        inputIdNumber = input("Enter ID Number to show details: ")

        if inputIdNumber in patientsData:
            print("Patient found:")
            patientsData[inputIdNumber].showDetails()
        else:   
            print("No patient found with that ID number.")
        
    elif choice == "3":
        print("Exiting the program.")
        break