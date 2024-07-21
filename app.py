from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Data JSON
dataMahasiswa = [
    {
        "id": 1,  
        "nama": "Rizky",
        "pendidikan": [
            {
                "universitas": "Universitas Gunadarma",
                "jurusan": "Informatika",
                "kelas": '1IA06',
                "npm": 51423007
            }
        ]
    },
    {
        "id": 2,  
        "nama": "Zechan",
        "pendidikan": [
            {
                "universitas": "Universitas Gunadarma",
                "jurusan": "Informatika",
                "kelas": '1IA06',
                "npm": 51423039
            }
        ]
    },
    {
        "id": 3,  
        "nama": "Naurah",
        "pendidikan": [
            {
                "universitas": "Universitas Gunadarma",
                "jurusan": "Informatika",
                "kelas": '1IA06',
                "npm": 51423089
            }
        ]
    },
    {
        "id": 4,  
        "nama": "Noval",
        "pendidikan": [
            {
                "universitas": "Universitas Gunadarma",
                "jurusan": "Informatika",
                "kelas": '1IA06',
                "npm": 51423119
            }
        ]
    },
    {
        "id": 5,  
        "nama": "Raffael",
        "pendidikan": [
            {
                "universitas": "Universitas Gunadarma",
                "jurusan": "Informatika",
                "kelas": '1IA06',
                "npm": 51423180
            }
        ]
    },
    {
        "id": 6,  
        "nama": "Razi",
        "pendidikan": [
            {
                "universitas": "Universitas Gunadarma",
                "jurusan": "Informatika",
                "kelas": '1IA06',
                "npm": 51423257
            }
        ]
    },
    {
    "id": 7,  
    "nama": "Thomas",
    "pendidikan": [
        {
            "universitas": "Universitas Gunadarma",
            "jurusan": "Informatika",
            "kelas": "1IA06",
            "npm": 51423300
        }
    ]
}

]

# Primary Route / Home
@app.route('/')
def home():
    return render_template('index.html')

# Endpoint JSON Access / menampilkan semua nama
@app.route('/datajson', methods=['GET', 'POST'])
def dataJson():
    if request.method == 'POST':
        new_data = request.get_json()
        dataMahasiswa.append(new_data)
        return jsonify({"result": "Data added successfully"}), 201
    return render_template('datajson.html', data=dataMahasiswa)

# ID Filtering JSON
@app.route('/datajson/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def filteringId(id):
    data = next((item for item in dataMahasiswa if item["id"] == id), None)
    if request.method == 'GET':
        if data:
            return jsonify({"result": data})
        return jsonify({"Error": "Data not found"}), 404
    elif request.method == 'PUT':
        updated_data = request.get_json()
        if data:
            index = dataMahasiswa.index(data)
            dataMahasiswa[index] = updated_data
            return jsonify({"result": "Data updated successfully"})
        return jsonify({"Error": "Data not found"}), 404
    elif request.method == 'DELETE':
        if data:
            dataMahasiswa.remove(data)
            return jsonify({"result": "Data deleted successfully"})
        return jsonify({"Error": "Data not found"}), 404

# Route untuk menambahkan dataMahasiswa form HTML
@app.route('/add_student', methods=['GET'])
def add_student():
    return render_template('add_student.html')

# Route untuk menampilkan form HTML penghapusan by ID
@app.route('/del_student', methods=['GET'])
def delete_student_by_id():
    return render_template('del_student.html')

# Endpoint untuk menghapus data mahasiswa berdasarkan ID
@app.route('/datajson/<int:id>', methods=['DELETE'])
def delete_student(id):
    data = next((item for item in dataMahasiswa if item["id"] == id), None)
    if data:
        dataMahasiswa.remove(data)
        return jsonify({"result": "Data deleted successfully"}), 200
    return jsonify({"error": "Data not found"}), 404

# Route untuk menampilkan form HTML edit data
@app.route('/edit_student', methods=['GET'])
def edit_student():
    return render_template('edit_student.html')

# Endpoint untuk mendapatkan data mahasiswa berdasarkan ID
@app.route('/datajson/<int:id>', methods=['GET'])
def get_student(id):
    data = next((item for item in dataMahasiswa if item["id"] == id), None)
    if data:
        return jsonify(data), 200
    return jsonify({"error": "Data not found"}), 404

# Endpoint untuk memperbarui data mahasiswa berdasarkan ID
@app.route('/datajson/<int:id>', methods=['PUT'])
def update_student(id):
    data = next((item for item in dataMahasiswa if item["id"] == id), None)
    if data:
        updated_data = request.get_json()
        data['nama'] = updated_data['nama']
        data['pendidikan'][0]['universitas'] = updated_data['pendidikan'][0]['universitas']
        data['pendidikan'][0]['jurusan'] = updated_data['pendidikan'][0]['jurusan']
        data['pendidikan'][0]['kelas'] = updated_data['pendidikan'][0]['kelas']
        data['pendidikan'][0]['npm'] = updated_data['pendidikan'][0]['npm']
        return jsonify({"result": "Data updated successfully"}), 200
    return jsonify({"error": "Data not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)