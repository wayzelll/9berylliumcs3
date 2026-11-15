class Patient:
    def __init__(self, name, billAmount):
        self.__name = name
        self.__billAmount = float(billAmount)
      
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_billAmount(self):
        return self.__billAmount

    def set_bill_amount(self, billAmount):
        self.__billAmount = float(billAmount)

    def calcbill(self):
        return self.__billAmount

    def display_patient_type(self):
        print("Patient Type: Regular Patient")

class SeniorPatient(Patient):
    def calcbill(self):
        return self.get_billAmount() * 0.80

    def display_patient_type(self):
        print("Patient Type: Senior Citizen")

class PhilhealthPatient(Patient):
    def calcbill(self):
        return self.get_billAmount() * 0.85

    def display_patient_type(self):
        print("Patient Type: PhilHealth Member")

print("Hospital Billing System")
print("-----------------------")

patients = [
    Patient("Juan Dela Cruz", 15000.00),
    SeniorPatient("Maria Santos", 15000.00),
    PhilhealthPatient("Pedro Reyes", 15000.00)
]
for patient in patients:
    print(f"Patient Name:  {patient.get_name()}")
    patient.display_patient_type()
    print(f"Original Bill: ₱{patient.get_billAmount():,.2f}")
    print(f"Final Bill: ₱{patient.calcbill():,.2f}\n")
