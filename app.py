from flask import Flask, render_template, request, redirect, url_for
import uuid

app = Flask(__name__)

# In-memory task storage (using unique IDs)
tasks = []

# Helper function to find a task by its unique ID
def find_task_by_id(task_id):
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None

# Home route - displays the To-Do list
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# Route to add a task
@app.route('/add', methods=['POST'])
def add_task():
    task_name = request.form.get('task_name')
    due_date = request.form.get('due_date')
    if task_name:
        tasks.append({
            "id": str(uuid.uuid4()),  # Generate a unique ID for each task
            "name": task_name,
            "completed": False,
            "due_date": due_date if due_date else None
        })
    return redirect(url_for('index'))

# Route to mark a task as completed
@app.route('/complete/<task_id>')
def complete_task(task_id):
    task = find_task_by_id(task_id)
    if task:
        task['completed'] = True
    return redirect(url_for('index'))

# Route to delete a task
@app.route('/delete/<task_id>')
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]  # Remove task by ID
    return redirect(url_for('index'))

# Route to edit a task
@app.route('/edit/<task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = find_task_by_id(task_id)
    if not task:
        return "Task not found", 404  # Return a 404 error if the task_id is not found

    if request.method == 'POST':
        task['name'] = request.form.get('task_name')
        task['due_date'] = request.form.get('due_date') if request.form.get('due_date') else None
        return redirect(url_for('index'))

    return render_template('edit.html', task=task, task_id=task_id)

if __name__ == "__main__":
    app.run(debug=True)
