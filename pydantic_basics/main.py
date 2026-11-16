# Steps to create and run your Pydantic Model
#     1. Define your Pydantic Model
#     2. Create an Object of this Pydantic Model
#     3. Throw your data to this Object
#     4. Then run to check if there is no ValidationError
#     -> Here we can call Pydantic Model as Pydantic Class as well

"""
1. Type validation = List, Dict, Optional
"""

from pydantic import BaseModel
from typing import List, Dict, Optional

class Patient(BaseModel):
    name : str
    age : int
    allergies : Optional[List[str]] = None
    contact_details : Dict[str, str]

def insert_patient_data(patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print("Inserted to DB")

info = {"name" : "Punith", "age" : "30", "allergies" : ["pollen", "dust"], "contact_details" : {"abc" : "abc@mail.com", "xyz" : "xyz@mail.com"}}
patient = Patient(**info)

insert_patient_data(patient)