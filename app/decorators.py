from functools import wraps

from flask import abort
from flask_login import current_user

from .models import Permission


def permission_required(permission):
    """Restrict a view to users with the given permission."""

    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)

        return decorated_function

    return decorator


def admin_required(f):
    return permission_required(Permission.ADMINISTER)(f)


def organization_required(f):
    return permission_required(Permission.ORGANIZATION)(f)


def educator_required(f):
    return permission_required(Permission.EDUCATOR)(f)
