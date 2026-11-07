from fastapi import FastAPI, HTTPException

app = FastAPI()

students = [
    {"id": 1, "name": "Punith", "course": "Python", "age": 23},
    {"id": 2, "name": "Rahul", "course": "Java", "age": 22},
    {"id": 3, "name": "Kiran", "course": "Python", "age": 24}
]

@app.get("/students")
def view_students(course : str = None, age : int = None):
    if age == None and course == None:
        return students

    res = []
    for student in students:
        if student["course"] == course or student["age"] == age:
            res.append(student)
    return res

@app.get("/students/{student_id}")
def view_students(student_id : int):
    for student in students:
        if student['id'] == student_id:
            return student

    raise HTTPException(400, detail="Error Data not Found")

    
