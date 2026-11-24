from pydantic import BaseModel
from typing import List, Dict

class Address(BaseModel):
    city: str
    dist: str
    pincode: int

class Patient(BaseModel):
    name: str
    age: int = 21
    email: str
    address: Address

address_info = {
    'city': 'Bdvt',
    'dist': 'Smg',
    'pincode': '577301'
}

info = {
    'name': 'Punith',
    # 'age': 21,
    'email': 'punith@axis.com',
    'address': address_info
}

p = Patient(**info)
tmp = p.model_dump(include=['name', 'age'])
tmp = p.model_dump(exclude=['name', 'age'])
tmp = p.model_dump(exclude={'address': ['city']})
tmp = p.model_dump(exclude_unset=True)
print(tmp)
print(type(tmp))