from hmac import compare_digest
from user import User

users = [
    User(1, 'user1', 'abcxyz'),
    User(2, 'user2', '123456'),
]

# Set Comprehension
username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    # If there isn't a username, return None
    user = username_table.get(username, None)
    if user and compare_digest(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)
