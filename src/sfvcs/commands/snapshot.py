import base64
from datetime import datetime
import json

import bsdiff4

from sfvcs.models.blob import Blob
from sfvcs.models.cas_store import CasStore
from sfvcs.models.commit import Commit
from sfvcs.utils.errors import NoChangesError
from sfvcs.utils.hash import hash_content
from sfvcs.utils.ref import update_head, get_ref


def create_blob(content=None, base=None, delta=None):
    id = hash_content(f"{content} {base} {delta}")
    blob = Blob(id=id, payload=content, delta=delta, base=base)
    CasStore.save_object(blob)
    return blob.id

def create_commit(parent, entry, metadata):
    id = hash_content(f"{parent} {entry} {metadata}")
    commit = Commit(id=id, parent=parent, payload=entry, metadata=metadata)
    CasStore.save_object(commit)
    return commit

def reconstruct(id: str):
    blob = None
    with open(f"{CasStore.get_object_store_location()}/{id}.json") as f:
        blob = json.load(f)
    parent = blob.get("base")
    content = blob.get("payload")
    delta = blob.get("delta")
    current_bytes = content.encode("utf-8") if content else base64.b64decode(delta.encode("utf-8"))
    if not parent:
        return current_bytes
    reconstructed_content = bsdiff4.patch(reconstruct(blob.get("base")), current_bytes)
    return reconstructed_content

def has_changes(parent_id, content):
    return reconstruct(parent_id) != content

def create_snapshot(message: str):
    ref = get_ref()
    tracked_file_path = ref["index"]
    head = ref.get("head")

    with open(tracked_file_path) as f:
        file_content = f.read()
    if not head:
        blob_id = create_blob(content=file_content)
        commit_meta = {
            "message": message,
            "timestamp": datetime.now().isoformat(timespec="seconds")
        }
        commit_id = create_commit(parent=head, entry=blob_id, metadata=commit_meta)
        update_head(commit_id)
        return

    # reconstruct prv file and store diff
    with open(f"{CasStore.get_object_store_location()}/{head}.json") as f:
        commit_obj = json.load(f)
        parent_blob_id = commit_obj.get("payload")
    # reconstruct from parent_blob_id to first base
    if not has_changes(parent_blob_id, file_content.encode()):
        raise NoChangesError("No changes to commit")

    diff = bsdiff4.diff(reconstruct(parent_blob_id), file_content.encode())
    patch_b64 = base64.b64encode(diff).decode("utf-8")

    blob_id = create_blob(base=parent_blob_id, delta=patch_b64)
    commit_meta = {
        "message": message,
        "timestamp": datetime.now().isoformat(timespec="seconds")
    }
    commit_obj = create_commit(parent=head, entry=blob_id, metadata=commit_meta)
    update_head(commit_obj.id)
    return commit_obj
