import json
import os
from datetime import datetime

from sfvcs.commands.snapshot import reconstruct
from sfvcs.models.cas_store import CasStore
from sfvcs.utils.ref import update_head, get_ref


def checkout_snapshot(commit_id: str):
    store_dir = CasStore.get_object_store_location()
    commit_path = os.path.join(store_dir, f"{commit_id}.json")

    if not os.path.exists(commit_path):
        raise ValueError(f"✖ Commit {commit_id} not found.")

    with open(commit_path) as f:
        commit = json.load(f)

    # Reconstruct file content
    content_bytes = reconstruct(commit["payload"])

    # Get the tracked filename from metadata
    tracked_file = get_ref().get("index")
    with open(tracked_file, "wb") as f:
        f.write(content_bytes)

    update_head(commit_id)

    ts = datetime.fromisoformat(commit["metadata"]["timestamp"])
    print(f"✔ Checked out commit {commit_id}")
    print(f"  Message: {commit['metadata']['message']}")
    print(f"  Date: {ts.strftime('%b %d, %Y %H:%M:%S')}")
    print(f"  Restored: {tracked_file}")