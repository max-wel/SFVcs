class Blob:
    def __init__(self, id: str, payload: str, delta: str | None, base: str | None):
        self.id = id
        self.payload = payload
        self.type = "blob"
        self.delta = delta
        self.base = base

    def to_dict(self):
        return {
            "id": self.id,
            "payload": self.payload,
            "type": self.type,
            "delta": self.delta,
            "base": self.base
        }
