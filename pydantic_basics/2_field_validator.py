from pydantic import BaseModel, field_validator
from typing import List, Dict

class Patient(BaseModel):
    name: str
    age: int
    email: str
    allergies: List[str]
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        name, mail = value.split('@')

        if mail not in ['axis.com', 'sbi.com']:
            raise ValueError('Not a valid domain')

        return value

    @field_validator('name')
    @classmethod
    def name_transform(cls, value):
        return value.upper()

    @field_validator('age', mode='before')
    @classmethod
    def age_validate(cls, value):
        return value if 0 < value < 100 else ValueError("Not Supported")

def get_info(patient):
    print(patient.name)
    print(patient.age)

info = {
    'name': 'Punith',
    'age': 21,
    'email': 'punith@axis.com',
    'allergies': ['pollen', 'dust'],
    'contact_details': {'abc' : '12345', 'cde':'23456'}
}

patient = Patient(**info)
get_info(patient)