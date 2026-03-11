from core.users import create_user, add_user_to_group
from core.groups import create_group
from core.tasks import create_task, submit_task, task_status
from datetime import datetime, timedelta

# Create users
create_user("u1", "Alice")
create_user("u2", "Bob")

# Create group
gid = create_group("DSA Group", "u1")

add_user_to_group("u2", gid)

# Create task
tid = create_task(
    gid,
    "LeetCode Two Sum",
    "https://leetcode.com/problems/two-sum/",
    datetime.now() + timedelta(days=1)
)

# Submit task
submit_task(tid, "u1")

print(task_status(tid))
