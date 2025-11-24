# vcs/errors.py
class RepoNotInitializedError(Exception):
    pass

class FileNotTrackedError(Exception):
    pass

class NoChangesError(Exception):
    pass
