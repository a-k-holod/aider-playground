from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for todos
todos = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        todo_item = request.form.get('todo')
        if todo_item:
            todos.append(todo_item)
    return render_template('index.html', todos=todos, enumerate=enumerate)

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(todos):
        del todos[index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
