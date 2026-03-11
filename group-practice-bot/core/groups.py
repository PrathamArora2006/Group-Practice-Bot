from storage.memory_store import groups
from utils.ids import generate_id

def create_group(name: str, admin_id: str):
    group_id = generate_id()

    groups[group_id] = {
        "name": name,
        "admin": admin_id,
        "members": set([admin_id]),
        "tasks": set()
    }

    return group_id

def get_groups(group_ids: str):
    return groups.get(group_ids)

def add_member(group_id: str, user_id: str):
    if group_id not in groups:
        raise ValueError("Group does not exist")
    
    groups[group_id]["members"].add(user_id)

