# models.py

class Task:
    def __init__(self, id, title, completed=False):
        self.id = id
        self.title = title
        self.completed = completed

# In-memory list to store tasks
tasks = []
task_id_counter = 1  # Counter to assign unique IDs to tasks
