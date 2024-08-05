from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = ['mysql+mysqlconnector://root:{*passwordenterhere}@localhost/GymDatabase']
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Member(db.Model):
    __tablename__ = 'Members'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer)


class WorkoutSession(db.Model):
    __tablename__ = 'WorkoutSessions'
    session_id = db.Column(db.Integer, primary_key=True)
    member_id = db.Columnn(db.Integer, db.ForeignKey('Members.id'))
    session_date = db.Column(db.Date, nullable=False)
    session_time = db.Column(db.String(50) ,nullable=False)
    activity= db.Column(db.String(255), nullable=False)
    member = db.relationship('Member', backref= db.backref('WorkoutSessions'))


@app.route('/Members', methods=['POST'])
def add_member():
    name = request.json['name']
    age = request.json['age']
    new_member = Member(name=name, age=age)
    db.session.add(new_member)
    db.session.commit()
    return jsonify({"message": "New member added successfully"}), 201


@app.route('/Members/<int:id>', methods=['GET'])
def get_member():
    all_members = Member.query(all)
    result = Member.dump(all_members)
    return jsonify(result)

@app.route('/Members/<int:id>', methods=['DELETE'])
def delete_member(id):
    member = Member.query.get_or_404(id)
    db.session.delete(member)
    db.session.commit()
    return jsonify({"message": "Member deleted successfully."}), 200  


@app.route('/Members/<int:id>', methods=['PUT'])
def update_member():
    member = Member.query.get_or_404(id)
    name = request.json['name']
    age = request.json['age']
    member.name = name
    member.age = age
    db.session.commit()
    return jsonify(member)
 

@app.route('/WorkoutSessions', methods=['POST'])
def add_workoutsession():
    member_id = request.json['member_id']
    session_date = request.json['session_date']
    session_time = request.json['session_time']
    activity = request.json['activity']
    new_workout = WorkoutSession(member_id=member_id, session_date=session_date, session_time=session_time, activity=activity)
    db.session.add(new_workout)
    db.session.commit()
    return jsonify({"message": "New workout added successfully"}), 201
   

@app.route('/WorkoutSessions/<int:id>', methods=['GET'])
def get_workoutsession(session_id):
    all_sessions = WorkoutSession.query(all)
    result = WorkoutSession.dump(all_sessions)
    return jsonify(result)

@app.route('/Members/<int:id>', methods=['PUT'])
def update_session():
    workout = WorkoutSession.query.get_or_404(id)
    session_date = request.json['session_date']
    session_time = request.json['session_time']
    activity = request.json['activity']
    workout.session_date = session_date
    workout.session_time = session_time
    workout.activity = activity
    db.session.commit()
    return jsonify(workout)

@app.route('/WorkoutSession /<int:id>', methods=['DELETE'])
def delete_session(session_id):
    workout = WorkoutSession.query.get_or_404(session_id)
    db.session.delete(workout)
    db.session.commit()
    return jsonify({"message": "Workout deleted successfully."}), 200  


@app.route('/WorkoutSession /<int:id>', methods=['GET'])
def workout_session_for_member(member_id):
    workouts = WorkoutSession.query.filter_by(member_id=member_id).all()
    return jsonify([{'session_id': workout.session_id, 'member_id': workout.member_id, 'session_date': workout.session_time, 'session_date': workout.session_time, "activity": workout.actvity} for workout in workouts])
   

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
