import json
from datetime import datetime

from sfvcs.utils.ref import get_ref
from sfvcs.models.cas_store import CasStore


def show_commits():
    head = get_ref().get("head")

    while head:
        path = f"{CasStore.get_object_store_location()}/{head}.json"
        with open(path) as f:
            commit = json.load(f)
        ts_str = commit['metadata']['timestamp']
        dt = datetime.fromisoformat(ts_str)  # convert to datetime object
        human_readable = dt.strftime("%b %d, %Y %H:%M:%S")

        print(f"Commit ID -> {commit['id']}")
        print(f"Date      -> {human_readable}")
        print(f"Message   -> {commit['metadata']['message']}")
        print("")

        head = commit.get("parent")