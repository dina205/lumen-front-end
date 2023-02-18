from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)
    contact_name = db.Column(db.String(100), nullable=False)
    contact_gender = db.Column(db.String(10), nullable=False)
    contact_email = db.Column(db.String(100), nullable=False)
    contact_mobile = db.Column(db.String(20), nullable=False)
    contact_address = db.Column(db.String(500), nullable=False)
    event_type = db.Column(db.String(10), nullable=False)
    event_location = db.Column(db.String(500), nullable=True)
    seats_available = db.Column(db.Integer, nullable=False)


@app.route('/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    return jsonify([event.serialize() for event in events])


@app.route('/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    event = Event.query.filter_by(id=event_id).first()
    if event:
        return jsonify(event.serialize())
    else:
        return jsonify({'error': 'Event not found'})


@app.route('/events', methods=['POST'])
def create_event():
    event_data = request.get_json()
    new_event = Event(name=event_data['name'], description=event_data['description'],
                      datetime=event_data['datetime'], contact_name=event_data['contact_name'],
                      contact_gender=event_data['contact_gender'], contact_email=event_data['contact_email'],
                      contact_mobile=event_data['contact_mobile'], contact_address=event_data['contact_address'],
                      event_type=event_data['event_type'], event_location=event_data['event_location'],
                      seats_available=event_data['seats_available'])
    db.session.add(new_event)
    db.session.commit()
    return jsonify(new_event.serialize())


@app.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    event_data = request.get_json()
    event = Event.query.filter_by(id=event_id).first()
    if event:
        event.name = event_data['name']
        event.description = event_data['description']
        event.datetime = event_data['datetime']
        event.contact_name = event_data['contact_name']
        event.contact_gender = event_data['contact_gender']
        event.contact_email = event_data['contact_email']
        event.contact_mobile = event_data['contact_mobile']
        event.contact_address = event_data['contact_address']
        event.event_type = event_data['event_type']
        event.event_location = event_data['event_location']
        event.seats_available = event_data['seats_available']
        db.session.commit()
        return jsonify(event.serialize())
    else:
        return jsonify({'error': 'Event not found'})


@app.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    event = Event.query.filter_by(id=event_id).first()
    if event:
        db.session.delete(event)
        db.session.commit()
        return jsonify({'message': 'Event deleted'})
    else:
        return jsonify({'error': 'Event not found'})


if __name__ == '__main__':
    app.run(debug=True)
