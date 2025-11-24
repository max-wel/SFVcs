import os

from sfvcs.utils.errors import RepoNotInitializedError

VCS_DIR = ".vcs/"
def init_repo():
    if os.path.exists(VCS_DIR):
        raise RepoNotInitializedError("⚠️ Repository already initialized.")
    os.makedirs(VCS_DIR, exist_ok=True)

def get_vcs_dir():
    return VCS_DIR