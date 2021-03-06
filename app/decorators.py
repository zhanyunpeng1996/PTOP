from functools import wraps
from flask import abort,redirect,url_for
from flask_login import current_user
from .models import Permission


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_funtion(*args, **kwargs):
            if not current_user.can(permission):
                return redirect(url_for('admin.admin_login'))
            return f(*args, **kwargs)
        return decorated_funtion
    return decorator


def admin_required(f):
    return permission_required(Permission.ADMINISTER)(f)
