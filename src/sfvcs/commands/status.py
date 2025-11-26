import json

from sfvcs.commands.snapshot import has_changes
from sfvcs.models.cas_store import CasStore
from sfvcs.utils.errors import NoChangesError
from sfvcs.utils.ref import get_ref


def show_status():
    ref = get_ref()
    tracked_file_path = ref["index"]
    head = ref.get("head")

    if not head:
        print(f"🕐 Tracking '{tracked_file_path}', but no commits yet.")
        return

    with open(f"{CasStore.get_object_store_location()}/{head}.json") as f:
        commit = json.load(f)
        blob_id = commit["payload"]

    with open(tracked_file_path, "rb") as f:
        target_bytes = f.read()

    if not has_changes(blob_id, target_bytes):
        return f"No changes detected in '{tracked_file_path}'."
    else:
        return f"⚠ Changes detected in '{tracked_file_path}' — ready to commit."