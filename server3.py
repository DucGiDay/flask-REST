# Required imports
import uuid
import os
from datetime import date
from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app
from flask_cors import CORS, cross_origin


# Initialize Flask app
app = Flask(__name__)

# Apply flask Cors
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Initialize Firestore DB
cred = credentials.Certificate('webgolang.json')
default_app = initialize_app(cred)
db = firestore.client()

##################################
# Route DKT
dkt_ref = db.collection('Category_Dang_Kien_Thuc')
@app.route('/api/dkt', methods=['POST'])
@cross_origin(origin='*')
def create():
    try:
        # id = request.json['id']
        idRef = str(uuid.uuid4())
        dkt_ref.document(idRef).set(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"

@app.route('/api/dkt', methods=['GET'])
@cross_origin(origin='*')
def read():
    try:
        # Check if ID was passed to URL query
        todo_id = request.args.get('id')
        if todo_id:
            todo = dkt_ref.document(todo_id).get()
            res = todo.to_dict()
            res["id"] = todo.id
            return jsonify(res), 200
        else:
            all_todos = []
            for doc in dkt_ref.stream():
                res = doc.to_dict()
                res["id"] = doc.id
                all_todos.append(res)
            return jsonify(all_todos), 200
    except Exception as e:
        return f"An Error Occurred: {e}"

@app.route('/api/dkt', methods=['PUT'])
@cross_origin(origin='*')
def update():
    try:
        id = request.args.get('id')
        dkt_ref.document(id).update(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"

@app.route('/api/dkt', methods=['DELETE'])
@cross_origin(origin='*')
def delete():
    try:
        # Check for ID in URL query
        todo_id = request.args.get('id')
        dkt_ref.document(todo_id).delete()
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"

############################
#Route DVKT
dvkt_ref = db.collection('Category_Don_vi_kien_thuc')
@app.route('/api/dvkt', methods=['POST'])
@cross_origin(origin='*')
def createDVKT():
    try:
        # id = request.json['id']
        idRef = str(uuid.uuid4())
        dvkt_ref.document(idRef).set(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"

@app.route('/api/dvkt', methods=['GET'])
@cross_origin(origin='*')
def readDVKT():
    try:
        # Check if ID was passed to URL query
        todo_id = request.args.get('id')
        if todo_id:
            todo = dvkt_ref.document(todo_id).get()
            res = todo.to_dict()
            res["id"] = todo.id
            return jsonify(todo.to_dict()), 200
        else:
            all_todos = []
            for doc in dvkt_ref.stream():
                res = doc.to_dict()
                res["id"] = doc.id
                all_todos.append(res)
            return jsonify(all_todos), 200
    except Exception as e:
        return f"An Error Occurred: {e}"

@app.route('/api/dvkt', methods=['PUT'])
@cross_origin(origin='*')
def updateDVKT():
    try:
        id = request.args.get('id')
        dvkt_ref.document(id).update(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"

@app.route('/api/dvkt', methods=['DELETE'])
@cross_origin(origin='*')
def deleteDVKT():
    try:
        # Check for ID in URL query
        todo_id = request.args.get('id')
        dvkt_ref.document(todo_id).delete()
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"


############################
#Route MTCT
mtct_ref = db.collection('Category_mo_ta_chi_tiet')
@app.route('/api/chi-tiet', methods=['POST'])
@cross_origin(origin='*')
def createMTCT():
    try:
        # id = request.json['id']
        idRef = str(uuid.uuid4())
        mtct_ref.document(idRef).set(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"

@app.route('/api/chi-tiet', methods=['GET'])
@cross_origin(origin='*')
def readMTCT():
    try:
        # Check if ID was passed to URL query
        todo_id = request.args.get('id')
        if todo_id:
            todo = mtct_ref.document(todo_id).get()
            res = todo.to_dict()
            res["id"] = todo.id
            return jsonify(todo.to_dict()), 200
        else:
            all_todos = []
            for doc in mtct_ref.stream():
                res = doc.to_dict()
                res["id"] = doc.id
                all_todos.append(res)
            return jsonify(all_todos), 200
    except Exception as e:
        return f"An Error Occurred: {e}"

@app.route('/api/chi-tiet', methods=['PUT'])
@cross_origin(origin='*')
def updateMTCT():
    try:
        id = request.args.get('id')
        mtct_ref.document(id).update(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"

@app.route('/api/chi-tiet', methods=['DELETE'])
@cross_origin(origin='*')
def deleteMTCT():
    try:
        # Check for ID in URL query
        todo_id = request.args.get('id')
        mtct_ref.document(todo_id).delete()
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"


############################
#Route Câu hỏi
cauHoi_ref = db.collection('cau_Hoi')
@app.route('/api/cau-hoi', methods=['POST'])
@cross_origin(origin='*')
def createCauHoi():
    try:
        idRef = str(uuid.uuid4())
        # cauHoi = request.json
        # cauHoi['Date'] = date.now()
        # print("cauHoi", cauHoi)
        cauHoi_ref.document(idRef).set(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"

# @app.route('/api/cau-hoi', methods=['GET'])
# @cross_origin(origin='*')
# def readCauHoi():
#     try:
#         # Check if ID was passed to URL query
#         todo_id = request.args.get('id')
#         if todo_id:
#             todo = cauHoi_ref.document(todo_id).get()
#             res = todo.to_dict()
#             res["id"] = todo.id
#             return jsonify(todo.to_dict()), 200
#         else:
#             all_todos = []
#             for doc in cauHoi_ref.stream():
#                 res = doc.to_dict()
#                 res["id"] = doc.id
#                 all_todos.append(res)
#             return jsonify(all_todos), 200
#     except Exception as e:
#         return f"An Error Occurred: {e}"

@app.route('/api/cau-hoi', methods=['PUT'])
@cross_origin(origin='*')
def updateCauHoi():
    try:
        id = request.args.get('id')
        cauHoi_ref.document(id).update(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"



############################
#Route Câu hỏi kép
cauHoiKep_ref = db.collection('cau_Hoi')
@app.route('/api/cau-hoi-kep', methods=['POST'])
@cross_origin(origin='*')
def createCauHoiKep():
    try:
        # id = request.json['id']
        idRef = str(uuid.uuid4())
        cauHoiKep_ref.document(idRef).set(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"

# @app.route('/api/cau-hoi-kep', methods=['GET'])
# @cross_origin(origin='*')
# def readCauHoiKep():
#     try:
#         # Check if ID was passed to URL query
#         todo_id = request.args.get('id')
#         if todo_id:
#             todo = cauHoiKep_ref.document(todo_id).get()
#             res = todo.to_dict()
#             res["id"] = todo.id
#             return jsonify(todo.to_dict()), 200
#         else:
#             all_todos = []
#             for doc in cauHoiKep_ref.stream():
#                 res = doc.to_dict()
#                 res["id"] = doc.id
#                 all_todos.append(res)
#             return jsonify(all_todos), 200
#     except Exception as e:
#         return f"An Error Occurred: {e}"

@app.route('/api/cau-hoi-kep', methods=['PUT'])
@cross_origin(origin='*')
def updateCauHoiKep():
    try:
        id = request.args.get('id')
        cauHoiKep_ref.document(id).update(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"

@app.route('/api/cau-hoi-kep', methods=['DELETE'])
@cross_origin(origin='*')
def deleteCauHoiKep():
    try:
        # Check for ID in URL query
        todo_id = request.args.get('id')
        cauHoiKep_ref.document(todo_id).delete()
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"


################
#Route lấy cả 2 loại câu hỏi
bothCauHoi_ref = db.collection('cau_Hoi')
@app.route('/api/both-cau-hoi', methods=['GET'])
@cross_origin(origin='*')
def readCauHoiKep():
    try:
        # Check if ID was passed to URL query
        todo_id = request.args.get('id')
        if todo_id:
            todo = bothCauHoi_ref.document(todo_id).get()
            res = todo.to_dict()
            res["id"] = todo.id
            return jsonify(todo.to_dict()), 200
        else:
            all_todos = []
            for doc in bothCauHoi_ref.stream():
                res = doc.to_dict()
                res["id"] = doc.id
                all_todos.append(res)
            return jsonify(all_todos), 200
    except Exception as e:
        return f"An Error Occurred: {e}"

@app.route('/api/cau-hoi', methods=['DELETE'])
@cross_origin(origin='*')
def deleteCauHoi():
    try:
        # Check for ID in URL query
        todo_id = request.args.get('id')
        cauHoi_ref.document(todo_id).delete()
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"

port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)