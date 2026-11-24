from pydantic import BaseModel
from typing import List, Dict

class Address(BaseModel):
    city: str
    dist: str
    pincode: int

class Patient(BaseModel):
    name: str
    age: int
    email: str
    address: Address

address_info = {
    'city': 'Bdvt',
    'dist': 'Smg',
    'pincode': '577301'
}

info = {
    'name': 'Punith',
    'age': 21,
    'email': 'punith@axis.com',
    'address': address_info
}

p = Patient(**info)
print(p)