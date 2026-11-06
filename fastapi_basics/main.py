from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)

    return data

@app.get("/")
def home():
    return { "message" : "Hello World!" }

@app.get("/about")
def home():
    return { "about" : "This is about page" }

@app.get("/view")
def get_data():
    data = load_data()
    return data


# In FastAPI, Path parameters are mandatory by default, 
# whether you use Path(...), Path(), or neither.
@app.get("/patient/{patient_id}")
def view_patient(patient_id : str = Path(description="This is patient_id Field", example="P001")):
    data = load_data()

    if patient_id in data:
        return data[patient_id]

    raise HTTPException(400, detail="Error, Patient is not Found")

@app.get('/query')
def view_query(sort_by : str = Query(description="['height', 'weight', 'bmi']"), order : str = Query(description="['asc', 'desc']")):
    data = load_data()
    valid_fields = {'height', 'weight', 'bmi'}
    order = False if order == 'asc' else True

    if sort_by in valid_fields:
        return sorted(data.values(), key = lambda x : x[sort_by], reverse=order)

    raise HTTPException(400, detail="sort_by data is not found")

