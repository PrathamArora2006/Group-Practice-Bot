from storage.memory_store import users

def create_user(user_id, name):
    if user_id in users:
        return users[user_id]
    
    users[user_id] = {
        'name': name,
        'groups': set()
    }
    return users[user_id]
    
def get_user(user_id):
    return users.get(user_id)

def add_user_to_group(user_id, group_id):
    if user_id not in users:
        raise ValueError("User does not exist")
    
    users[user_id]['groups'].add(group_id)