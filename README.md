# To-Do List Web App

A simple To-Do List web application built with Flask that allows users to add, edit, mark as complete, and delete tasks. Tasks can also have optional due dates.

## Features

- Add tasks with an optional due date and time.
- Mark tasks as completed.
- Edit tasks (including task name and due date).
- Delete tasks from the list.
- Tasks are stored in memory for demonstration purposes.

## Technologies Used

- **Flask**: A lightweight web framework for Python.
- **Bootstrap**: For basic styling and responsiveness.
- **Python**: Backend logic and task management.
- **HTML/CSS**: Frontend structure and styling.

## Setup Instructions

### Prerequisites

- Python 3.x
- `pip` (Python package manager)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/TomGirr/todolist.git
   ```
2. Navigate to the project directory:

	```bash
	cd todolist
	```
 
3. Create and activate a virtual environment (optional but recommended):

	```bash
	python -m venv venv
	source venv/bin/activate  # On Windows: venv\Scripts\activate
	```

4. Install the required Python packages:

	```bash
	pip install -r requirements.txt
	```

## Running the Application

1. Start the Flask development server:

    ```bash
	python app.py
	```
2. Open your browser and go to:

	```arduino

    http://127.0.0.1:5000/
	```
## Usage

- Add Task: Use the form on the homepage to add a new task, with an optional due date.
- Mark as Complete: Click the "Complete" button next to a task to mark it as completed.
- Edit Task: Click the "Edit" button next to a task to update its name or due date.
- Delete Task: Click the "Delete" button next to a task to remove it from the list.

### Future Enhancements
- Add persistent storage (e.g., a database) to save tasks permanently. 
- User authentication to create personalized to-do lists.
- Task filtering by date or priority.
   
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

