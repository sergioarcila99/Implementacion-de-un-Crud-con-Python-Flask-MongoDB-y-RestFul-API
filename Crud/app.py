from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mydatabase'  # Cambia la URI de acuerdo a tu configuración
mongo = PyMongo(app)

@app.route('/')
def index():
    todos = mongo.db.todos.find()
    return render_template('index.html', todos=todos)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        todo_content = request.form['content']
        mongo.db.todos.insert_one({'content': todo_content})
        return redirect('/')
    else:
        return render_template('create.html')

@app.route('/update/<string:id>', methods=['GET', 'POST'])
def update(id):
    todo = mongo.db.todos.find_one_or_404({'_id': id})
    if request.method == 'POST':
        new_content = request.form['content']
        mongo.db.todos.update_one({'_id': id}, {'$set': {'content': new_content}})
        return redirect('/')
    else:
        return render_template('update.html', todo=todo)

@app.route('/delete/<string:id>')
def delete(id):
    mongo.db.todos.delete_one({'_id': id})
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
