# Endpoint Flask Beserta Filtering


# import library
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# data JSON mahasiswaa 
dataMahasiswa = [
    {
        "id": 1,  
        "nama": "Rizky",
        "pendidikan": [
            {
                "universitas": "Gunadarma",
                "jurusan": "Informatika",
                "kelas": '1',
                "npm": 51004200
            }
        ]
    },
    {
        "id": 2,  
        "nama": "Zechan",
        "pendidikan": [
            {
                "universitas": "Gunadarma",
                "jurusan": "Informatika",
                "kelas": '1',
                "npm": 51004201
            }
        ]
    },
    {
        "id": 3,  
        "nama": "Naurah",
        "pendidikan": [
            {
                "universitas": "Gunadarma",
                "jurusan": "Informatika",
                "kelas": '1',
                "npm": 51004203
            }
        ]
    },
    {
        "id": 4,  
        "nama": "Noval",
        "pendidikan": [
            {
                "universitas": "Gunadarma",
                "jurusan": "Informatika",
                "kelas": '1',
                "npm": 51004204
            }
        ]
    },
    {
        "id": 5,  
        "nama": "Raffael",
        "pendidikan": [
            {
                "universitas": "Gunadarma",
                "jurusan": "Informatika",
                "kelas": '1',
                "npm": 51004205
            }
        ]
    },
    {
        "id": 6,  
        "nama": "Razi",
        "pendidikan": [
            {
                "universitas": "Gunadarma",
                "jurusan": "Informatika",
                "kelas": '1',
                "npm": 51004206
            }
        ]
    },
    {
        "id": 7,  
        "nama": "Thomas",
        "pendidikan": [
            {
                "universitas": "Gunadarma",
                "jurusan": "Informatika",
                "kelas": "1",
                "npm": 51004207
            }
        ]
    }
]

# primary route / home / tampilan awalnyaa
@app.route('/')
def home():
    # ngerender template HTML index.html buat route root
    return render_template('index.html')

# endpoint JSON access / menampilkan semua nama
@app.route('/datajson', methods=['GET', 'POST'])
def dataJson():
    if request.method == 'POST':
        # mengambil data JSON dari permintaan dan menambahkannya ke dataMahasiswa
        new_data = request.get_json()
        dataMahasiswa.append(new_data)
        return jsonify({"result": "Data added successfully"}), 201
    # ngerender template HTML datajson.html dengan dataMahasiswa
    return render_template('datajson.html', data=dataMahasiswa)

# crudnya ini pake filtering endpoint buat ngambil id user
@app.route('/datajson/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def filteringId(id):
    
    # nyarii data mahasiswa berdasarkan ID
    data = next((item for item in dataMahasiswa if item["id"] == id), None)
    if request.method == 'GET':
        # mengembalikan data mahasiswa jika ditemukann
        if data:
            return jsonify({"result": data})
        # mengembalikan pesan kesalahan jikaa data tidak ditemukan
        return jsonify({"Error": "Data not found"}), 404
    
    elif request.method == 'PUT':
        # MEMPERBARUI data mahasiswa jika ditemukan
        updated_data = request.get_json()
        if data:
            index = dataMahasiswa.index(data)
            dataMahasiswa[index] = updated_data
            return jsonify({"result": "Data updated successfully"})
        return jsonify({"Error": "Data not found"}), 404
    
    elif request.method == 'DELETE':
        # NGEHAPUS data mahasiswa jika ditemukan
        if data:
            dataMahasiswa.remove(data)
            return jsonify({"result": "Data deleted successfully"})
        return jsonify({"Error": "Data not found"}), 404


# Route buat nambahin dataMahasiswa form HTML
@app.route('/add_student', methods=['GET'])
def add_student():
    # ngerender template HTML add_student.html untuk NAMBAHIN data mahasiswa
    return render_template('add_student.html')

# Route buatt menampilkan form HTML penghapusan
@app.route('/del_student', methods=['GET'])
def delete_student_by_id():
    # ngerender template HTML del_student.html untuk HAPUS data mahasiswa berdasarkan ID
    return render_template('del_student.html')

# Endpoint buat menghapuss data mahasiswa berdasarkan ID
@app.route('/datajson/<int:id>', methods=['DELETE'])
def delete_student(id):
    # ncari data mahasiswa berdasarkan ID
    data = next((item for item in dataMahasiswa if item["id"] == id), None)
    # nghapuss data mahasiswa kalo ditemukan
    if data:
        dataMahasiswa.remove(data)
        return jsonify({"result": "Data deleted successfully"}), 200
    return jsonify({"error": "Data not found"}), 404

# Route untuk menampilkan form HTML edit data
@app.route('/edit_student', methods=['GET'])
def edit_student():
    # ngerenderr template HTML edit_student.html untuk EDIT data mahasiswa
    return render_template('edit_student.html')

# Endpoint untuk mendapatkan data mahasiswa berdasarkan ID
@app.route('/datajson/<int:id>', methods=['GET'])
def get_student(id):
    # Mencari data mahasiswa berdasarkan ID
    data = next((item for item in dataMahasiswa if item["id"] == id), None)
    # memperbarui data mahasiswa jika ditemukannn
    if data:
        return jsonify(data), 200
    return jsonify({"error": "Data not found"}), 404

# Endpoint buat memperbarui data mahasiswa berdasarkann ID
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

# menjalankan aplikasi Flask dalam mode debug
if __name__ == '__main__':
    app.run(debug=True)

