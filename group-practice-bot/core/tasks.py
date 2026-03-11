from datetime import datetime
from storage.memory_store import tasks, groups
from utils.ids import generate_id

def create_task(group_id: str, title: str, link: str, deadline: datetime):
    if group_id not in groups:
        raise ValueError("Group does not exist")
    
    task_id = generate_id()

    tasks[task_id] = {
        "title": title,
        "link": link,
        "deadline": deadline,
        "group_id": group_id,
        "submissions": {}
    }

    groups[group_id]["tasks"].add(task_id)
    return task_id 

def submit_task(task_id: str, user_id: str):
    if task_id not in tasks:
        raise ValueError("Task does not exist")
    
    tasks[task_id]["submissions"][user_id] = datetime.now()

def task_status(task_id: str):
    if task_id not in tasks:
        raise ValueError("Task does not exist")
    
    task = tasks[task_id]
    total = len(groups[task["group_id"]]["members"])
    completed = len(task["submissions"])

    return {
        "completed": completed,
        "total": total, 
        "percentage": (completed / total) * 100 if total > 0 else 0
    }