# -To-Do-List-App-using-Django
This is a simple web-based To-Do List application built using Django. The app allows users to create and manage their tasks, set due dates, add descriptions, and track the status of each task.

Features
Create a new task with a title, description, and optional due date
Edit the title, description, and due date of an existing task
Delete a task
Set tags for tasks to categorize them
Track the status of tasks (Open, Working, Done, Overdue)
Django Admin interface for easy management and validation checks
RESTful APIs for creating, reading, updating, and deleting tasks
Basic Authentication support for API access.

Installation
1. Clone the repository:
 git clone https://github.com/your-username/todo-list-app.git
 
 2. Change into the project directory: cd todo-list-app
 3. Install the required dependencies:pip install -r requirements.txt
 4. Run the Django development server: python manage.py runserver
 5. Access the app in your web browser at http://localhost:8000.
 
 Usage
To create a new task, click on the "Add Task" button and fill in the required information.
To edit a task, click on the task title and update the details.
To delete a task, click on the trash bin icon next to the task.
Use the Django Admin interface at http://localhost:8000/admin/ for advanced management and validation checks.

API Documentation
APIs are available for interacting with the To-Do List app. You can access the following endpoints:

POST /api/todo/: Create a new task.
GET /api/todo/: Retrieve all tasks.
GET /api/todo/{id}/: Retrieve a specific task.
PUT /api/todo/{id}/: Update a specific task.
DELETE /api/todo/{id}/: Delete a specific task.
Please refer to the provided Postman Collection for detailed API documentation and examples.

Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request. Make sure to follow the existing code style and guidelines.

License
This project is licensed under the MIT License.

Acknowledgements
This app was built using Django, a high-level Python web framework.
The RESTful APIs are implemented using Django REST Framework.
Basic Authentication support is provided by Django REST Framework.
Special thanks to the open-source community for their valuable contributions.
