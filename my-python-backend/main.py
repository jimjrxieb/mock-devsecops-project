from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Welcome to your FastAPI backend!'}

@app.get('/items/{item_id}')
def read_item(item_id: int, q: str = None):
    return {'item_id': item_id, 'q': q}

@app.route('/users', methods=['GET'])
def get_users_from_db():
    users_collection = db['users']
    users = list(users_collection.find({}, {'_id': 0}))
    return jsonify(users)
