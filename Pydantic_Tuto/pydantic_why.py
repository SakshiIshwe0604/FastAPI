from pydantic import BaseModel
from typing import List,Dict
# designed aa pydantic model
class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allerigies: List[str]
    contact_details: Dict[str,str]







# def insert_patient_data(patient: Patient):
#     print(patient.name)
#     print(patient.age)
#     print('inserted') 
# patient_info = {'name':'nitish','age':22}

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('updated') 
patient_info = {'name':'nitish','age':22,'weight': 75.2,'married':True,'allergies':['pollen','dust'], 
                'contact_details':{'email':'abc@gmail.com','phone':'9897979'}}

patient1 = Patient(**patient_info)

# insert_patient_data(patient1)
update_patient_data(patient1)