from pydantic import BaseModel, field_validator, computed_field
from typing import List, Dict

class Patient(BaseModel):
    name: str
    age: int
    email: str
    weight: float
    height: float
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        return self.height * self.weight

def get_info(patient):
    print(patient.name)
    print(patient.age)
    print('BMI', patient.bmi)

info = {
    'name': 'Punith',
    'age': 21,
    'email': 'punith@axis.com',
    'weight': 1.84,
    'height': 2.87,
    'allergies': ['pollen', 'dust'],
    'contact_details': {'abc' : '12345', 'cde':'23456'}
}

patient = Patient(**info)
get_info(patient)