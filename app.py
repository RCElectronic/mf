from flask import Flask, g, request, jsonify
from database import get_db
from functools import wraps


app = Flask(__name__)

api_username = 'admin'
api_password = 'ICTC-CTIC'

def protected(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == api_username and auth.password == api_password:
            return f(*args, **kwargs)
        return jsonify({'message' : 'Authentication failed!'}), 403
    return decorated    

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/teacher', methods=['GET'])
@protected
def get_teachers():
    db = get_db()
    teachers_cur = db.execute('select * from teachers')
    teachers = teachers_cur.fetchall()

    return_values = []
    for teacher in teachers:
        teacher_dict = {}
        teacher_dict['id'] = teacher['id']
        teacher_dict['first_name'] = teacher['first_name']
        teacher_dict['last_name'] = teacher['last_name']
        teacher_dict['email'] = teacher['email']
        teacher_dict['school'] = teacher['school'] 
        teacher_dict['submission'] = teacher['submission']
        teacher_dict['q1'] = teacher['q1']
        teacher_dict['q2'] = teacher['q2']
        teacher_dict['q3'] = teacher['q3']
        teacher_dict['q4'] = teacher['q4']
        teacher_dict['q5'] = teacher['q5']
        teacher_dict['q6'] = teacher['q6']
        teacher_dict['q7'] = teacher['q7']
        teacher_dict['q8'] = teacher['q8']
        teacher_dict['q9'] = teacher['q9']
        teacher_dict['q10'] = teacher['q10']
        teacher_dict['q11'] = teacher['q11']
        teacher_dict['q12'] = teacher['q12']
        teacher_dict['q13'] = teacher['q13']
        teacher_dict['q14'] = teacher['q14']
        teacher_dict['q15'] = teacher['q15']

        return_values.append(teacher_dict)

    return jsonify({'teachers' : return_values})


@app.route('/teacher/<int:teacher_id>', methods=['GET'])
@protected
def get_teacher(teacher_id):
    db = get_db()
    teacher_cur = db.execute('select id, first_name,last_name, email from teachers where id = ?', [teacher_id])
    teacher = teacher_cur.fetchone()

    return jsonify({'teacher' : {'id' : teacher['id'], 'first_name' : teacher['first_name'], 'last_name' : teacher['last_name'], 'email' : teacher['email'] } })

@app.route('/teacher', methods=['POST'])
@protected
def add_teacher():
    new_member_data = request.get_json()
    first_name = new_member_data['first_name']
    last_name = new_member_data['last_name']
    email = new_member_data['email']
    school = new_member_data['school']
    submission = new_member_data['submission']
    q1 = new_member_data['q1']
    q2 = new_member_data['q2']
    q3 = new_member_data['q3']
    q4 = new_member_data['q4']
    q5 = new_member_data['q5']
    q6 = new_member_data['q6']
    q7 = new_member_data['q7']
    q8 = new_member_data['q8']
    q9 = new_member_data['q9']
    q10 = new_member_data['q10']
    q11 = new_member_data['q11']
    q12 = new_member_data['q12']
    q13 = new_member_data['q13']
    q14 = new_member_data['q14']
    q15 = new_member_data['q15']

    db = get_db()
    db.execute('insert into teachers (first_name, last_name,email,school,submission,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', [first_name, last_name,email,school,submission,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15])
    db.commit()
    teacher_cur = db.execute('select id, first_name,last_name, email from teachers where first_name =?, last_name = ?', [first_name, last_name])
    teacher = teacher_cur.fetchone()
    return jsonify({'teacher' :{first_name,last_name,school,submission}})

@app.route('/teacher/<int:teacher_id>', methods=['PUT','PATCH'])
@protected
def edit_teacher(teacher_id):
    new_teacher_data = request.get_json()
    first_name = new_teacher_data['first_name']
    last_name = new_teacher_data['last_name']
    email = new_teacher_data['email']
    school = new_teacher_data['school']
    submission = new_teacher_data['submission']
    q1 = new_teacher_data['q1']
    q2 = new_teacher_data['q2']
    q3 = new_teacher_data['q3']
    q4 = new_teacher_data['q4']
    q5 = new_teacher_data['q5']
    q6 = new_teacher_data['q6']
    q7 = new_teacher_data['q7']
    q8 = new_teacher_data['q8']
    q9 = new_teacher_data['q9']
    q10 = new_teacher_data['q10']
    q11 = new_teacher_data['q11']
    q12 = new_teacher_data['q12']
    q13 = new_teacher_data['q13']
    q14 = new_teacher_data['q14']
    q15 = new_teacher_data['q15']

    db=get_db()
    db.execute('update teachers set first_name = ?, last_name = ?, email = ?, school = ?, submission = ?, q1 = ?, q2 = ?, q3 = ?, q4 = ?, q5 = ?, q6 = ?, q7 = ?, q8 = ?, q9 = ?, q10 = ?, q11 = ?, q12 = ?, q13 = ?, q14 = ?, q15 = ? where id = ?', [first_name, last_name,email,school,submission,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,teacher_id])
    db.commit()

    teachers_cur = db.execute('select id, first_name, last_name, email from teachers where id = ?', [teacher_id] )
    teacher = teachers_cur.fetchone()
    return jsonify({'teacher' : {'id' : teacher['id'], 'first_name' : teacher['first_name'], 'last_name' : teacher['last_name'], 'email' : teacher['email'] } })

@app.route('/teacher/<int:teacher_id>', methods=['DELETE'])
@protected
def delete_teacher(teacher_id):
    db=get_db()
    db.execute('delete from teachers where id =?', [teacher_id])
    db.commit()
    return jsonify({'message' : 'The teacher has been deleted!'})

if __name__ == '__main__':
    app.run(debug=True)