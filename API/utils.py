import json

from .models import User, TodoList


def json_validator(body):
    try:
        data = json.loads(body)
    except json.JSONDecodeError:
        return None, {'error': 'message not valid', 'status': 400}
    return data, None


def authenticate_user(request):
    token = request.headers.get('Authorization')
    if not token:
        return None, {'error': 'Token missing', 'status': 401}

    try:
        user = User.objects.get(token=request.headers.get('Authorization'))
        return user, None
    except User.DoesNotExist:
        return None, {'error': 'Invalid token', 'status': 401}


def validate_todo(todo_id, user):
    try:
        todo = TodoList.objects.get(id=todo_id)
    except TodoList.DoesNotExist:
        return None, {'error': 'invalid id', 'status': 401}

    if todo.author != user:
        return None, {'error': 'Unauthorized: You don\'t own this todo', 'status': 401}

    return todo, None
