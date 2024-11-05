# app.py

from flask import Flask, render_template, request, redirect, url_for
from models import Task, tasks, task_id_counter

app = Flask(__name__)


# Route to display all tasks
@app.route('/')
def task_list():
    return render_template('task_list.html', tasks=tasks)


# Route to add a new task
@app.route('/add', methods=['GET', 'POST'])
def add_task():
    global task_id_counter
    if request.method == 'POST':
        title = request.form['title']
        if title:
            new_task = Task(id=task_id_counter, title=title)
            tasks.append(new_task)
            task_id_counter += 1
            return redirect(url_for('task_list'))
    return render_template('add_task.html')


# Route to edit a task
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_task(id):
    task = next((t for t in tasks if t.id == id), None)
    if not task:
        return redirect(url_for('task_list'))

    if request.method == 'POST':
        task.title = request.form['title']
        task.completed = 'completed' in request.form
        return redirect(url_for('task_list'))

    return render_template('edit_task.html', task=task)


# Route to delete a task
@app.route('/delete/<int:id>', methods=['POST'])
def delete_task(id):
    global tasks
    tasks = [t for t in tasks if t.id != id]
    return redirect(url_for('task_list'))


if __name__ == '__main__':
    app.run(debug=True)
