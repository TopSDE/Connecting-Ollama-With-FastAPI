from pydantic import BaseModel, field_validator, model_validator
from typing import List, Dict

class Patient(BaseModel):
    name: str
    age: int
    email: str
    allergies: List[str]
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    def validate_model(self):
        if self.age > 60 and 'emergency' not in self.contact_details:
            raise ValueError('Patient >60 needs to have Emergency contact')
        return self

def get_info(patient):
    print(patient.name)
    print(patient.age)

info = {
    'name': 'Punith',
    'age': '61',
    'email': 'punith@axis.com',
    'allergies': ['pollen', 'dust'],
    'contact_details': {'abc':'12345', 'cde':'23456', 'emergency':'1234'}
}

patient = Patient(**info)
get_info(patient)