class Commit:
    def __init__(self, id, parent, payload, metadata):
        self.id = id
        self.parent = parent
        self.payload = payload
        self.metadata = metadata
        self.type = "commit"

    def to_dict(self):
        return {
            "id": self.id,
            "parent": self.parent,
            "type": self.type,
            "payload": self.payload,
            "metadata": self.metadata
        }