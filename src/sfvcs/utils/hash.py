import hashlib


def hash_content(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()