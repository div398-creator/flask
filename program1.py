from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory list to store data
data_store = []

# Create operation: Add a new item to the data store
@app.route('/create', methods=['POST'])
def create():
    new_item = request.json
    data_store.append(new_item)
    return jsonify(new_item), 201

# Read operation: Get all items from the data store
@app.route('/read', methods=['GET'])
def read():
    return jsonify(data_store), 200

# Update operation: Update an existing item in the data store
@app.route('/update/<int:item_id>', methods=['PUT'])
def update(item_id):
    if 0 <= item_id < len(data_store):
        data_store[item_id] = request.json
        return jsonify(data_store[item_id]), 200
    else:
        return jsonify({'error': 'Item not found'}), 404

# Delete operation: Delete an item from the data store
@app.route('/delete/<int:item_id>', methods=['DELETE'])
def delete(item_id):
    if 0 <= item_id < len(data_store):
        deleted_item = data_store.pop(item_id)
        return jsonify(deleted_item), 200
    else:
        return jsonify({'error': 'Item not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
