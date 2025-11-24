# vcs/decorators.py
import functools
import sys

from sfvcs.utils.errors import RepoNotInitializedError, FileNotTrackedError, NoChangesError
from sfvcs.utils.ui import error, warning


def safe_command(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            sys.exit(0)
        except (RepoNotInitializedError, FileNotTrackedError) as e:
            error(str(e))
            sys.exit(1)
        except NoChangesError as e:
            warning(str(e))
            sys.exit(1)
        except Exception as e:
            error(f"Unexpected error: {e}")
            sys.exit(2)
    return wrapper
