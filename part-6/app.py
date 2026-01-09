"""
Part 6: Homework - Personal To-Do List App
==========================================
See Instruction.md for full requirements.

How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data - your tasks list
TASKS = [
    {'id': 1, 'title': 'Learn Flask', 'status': 'Completed', 'priority': 'High'},
    {'id': 2, 'title': 'Build To-Do App', 'status': 'In Progress', 'priority': 'Medium'},
    {'id': 3, 'title': 'Push to GitHub', 'status': 'Pending', 'priority': 'Low'},
]


@app.route('/')
def index():
    """Home page - display all tasks"""
    return render_template('index.html', tasks=TASKS)

@app.route('/add', methods=['GET', 'POST'])
def add():
    """Page with a form to add new task, handles POST submissions"""
    if request.method == 'POST':
        title = request.form.get('title')
        status = request.form.get('status')
        priority = request.form.get('priority')
        if title and status and priority:
            new_id = max([t['id'] for t in TASKS]) + 1 if TASKS else 1
            TASKS.append({'id': new_id, 'title': title, 'status': status, 'priority': priority})
            return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/task/<int:id>')
def task(id):
    """View single task details"""
    # Find the task with matching id
    task = next((t for t in TASKS if t['id'] == id), None)
    return render_template('task.html', task=task)

@app.route('/about')
def about():
    """About the app page"""
    return render_template('about.html')

# Bonus: Filter by priority
@app.route('/priority/<name>')
def priority(name):
    """Filter tasks by priority"""
    filtered_tasks = [t for t in TASKS if t['priority'].lower() == name.lower()]
    return render_template('index.html', tasks=filtered_tasks, filter_priority=name)




if __name__ == '__main__':
    app.run(debug=True)
