from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Define a model for the items
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

# Create the database
with app.app_context():
    db.create_all()

# Create operation: Add a new item to the database
@app.route('/create', methods=['POST'])
def create():
    data = request.json
    new_item = Item(name=data['name'], description=data.get('description'))
    db.session.add(new_item)
    db.session.commit()
    return jsonify(new_item.to_dict()), 201

# Read operation: Get all items from the database
@app.route('/read', methods=['GET'])
def read():
    items = Item.query.all()
    return jsonify([item.to_dict() for item in items]), 200

# Update operation: Update an existing item in the database
@app.route('/update/<int:item_id>', methods=['PUT'])
def update(item_id):
    data = request.json
    item = Item.query.get(item_id)
    if item:
        item.name = data['name']
        item.description = data.get('description')
        db.session.commit()
        return jsonify(item.to_dict()), 200
    else:
        return jsonify({'error': 'Item not found'}), 404

# Delete operation: Delete an item from the database
@app.route('/delete/<int:item_id>', methods=['DELETE'])
def delete(item_id):
    item = Item.query.get(item_id)
    if item:
        db.session.delete(item)
        db.session.commit()
        return jsonify(item.to_dict()), 200
    else:
        return jsonify({'error': 'Item not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
