from flask import Flask, jsonify,request

app = Flask(__name__)

students = [
    {
        "name": "prit",
        "mail": "prit@gmail.com",
        "id": 1
    },
    {
        "name": "yash",
        "mail": "yash@gmail.com",
        "id": 2
    },
    {
        "name": "dev",
        "mail": "dev@gmail.com",
        "id": 3
    },
    {
        "name": "kamlesh",
        "mail": "kamlesh@gmail.com",
        "id": 4
    },
    {
        "name": "jash",
        "mail": "jash@gmail.com",
        "id": 5
    },
    {
        "name": "kunj",
        "mail": "kunj@gmail.com",
        "id": 6
    },
    {
        "name": "kartik",
        "mail": "kartik@gmail.com",
        "id": 7
    },
    {
        "name": "harsh",
        "mail": "harsh@gmail.com",
        "id": 8
    },
    {
        "name": "dhyey",
        "mail": "dhyey@gmail.com",
        "id": 9
    },
    {
        "name": "het",
        "mail": "het@gmail.com",
        "id": 10
    }
]

@app.route('/students')
def get_all_students():
    return jsonify({'students': students})

@app.route('/students/<int:id>')
def get_student(id):
    for student in students:
        if student ['id']== id:
            return jsonify(student)
    return jsonify({'message':'Student not found'})      

@app.route('/students',methods= ['POST']) 
def add_student():
        body_data = request.get_json()
        students.append(body_data)
        return jsonify({'message':'Student has been added'})

if __name__=="__main__":
    app.run(debug=True  )

