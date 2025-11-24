import json
import os

from sfvcs.commands.init import get_vcs_dir
from sfvcs.models.store_interface import StoreInterface


class CasStore(StoreInterface):
    location = f"{get_vcs_dir()}objects"

    @classmethod
    def save_object(cls, data):
        os.makedirs(cls.location, exist_ok=True)
        with open(f"{cls.location}/{data.id}.json", "w") as f:
            json.dump(data.to_dict(), f, indent=2)

    @classmethod
    def get_object_store_location(cls):
        return cls.location