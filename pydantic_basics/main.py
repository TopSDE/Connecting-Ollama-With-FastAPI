# Steps to create and run your Pydantic Model
#     1. Define your Pydantic Model
#     2. Create an Object of this Pydantic Model
#     3. Throw your data to this Object
#     4. Then run to check if there is no ValidationError
#     -> Here we can call Pydantic Model as Pydantic Class as well

"""
1. Type validation = List, Dict, Optional
2. Data validation = EmailStr, AnyUrl, Field, Annotated
3. Strict
4. Field validator:
    1.Additional data validation, Transformation
    2.Works on 2 Modes = 'before' and 'after'
"""

from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=5, description='This is Name Field')]
    age: int = Field(gt=0, lt=60, strict=True)
    email: EmailStr
    linkedin_url: AnyUrl
    allergies: Optional[List[str]] = Field(max_length=2)
    married: Annotated[bool, Field(default=None, description='This is either T or F')]
    contact_details: Dict[str, str]

def insert_patient_data(patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print("Inserted to DB")

info = {'name' : 'Punit', 'age' : 21, 'email' : 'abc@mail.com', 'linkedin_url' : 'https://google.com','allergies' : ["pollen", "dust"], 'married' : 1,'contact_details' : {"abc" : 'abc@mail.com', 'xyz' : 'xyz@mail.com'}}
patient = Patient(**info)

insert_patient_data(patient)