'''
Using decorators for authN
'''
from functools import wraps


def requires_permission(permission):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user = kwargs.get('user')
            if not user or permission not in user.permissions:
                raise PermissionError(
                    f'User doesnt have {permission} permission')
            return func(*args, **kwargs)
        return wrapper
    return decorator


class User:
    def __init__(self, permissions):
        self.permissions = permissions


@requires_permission("view_data")
def view_data(user):
    print("Data displayed")


@requires_permission("edit_data")
def edit_data(user):
    print("Data edited")


alice = User(permissions={"view_data"})
bob = User(permissions={"view_data", "edit_data"})

try:
    view_data(user=alice)  # Allowed
    view_data(user=bob)    # Allowed
    edit_data(user=alice)  # Uncomment to see PermissionError
    edit_data(user=bob)
except Exception as e:
    print("Error :", e)
