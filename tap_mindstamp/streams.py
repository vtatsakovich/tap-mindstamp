"""Stream type classes for tap-mindstamp."""

from pathlib import Path

from tap_mindstamp.client import MindstampStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

class VideosStream(MindstampStream):
    """Define custom stream."""
    name = "videos"
    path = "/videos"
    primary_keys = ["id"]
    replication_key = "updated_at"
    schema_filepath = SCHEMAS_DIR / "videos.json"
    has_pagination = False

class InteractionsStream(MindstampStream):
    """Define custom stream."""
    name = "interactions"
    path = "/interactions"
    primary_keys = ["id"]
    replication_key = "updated_at"
    schema_filepath = SCHEMAS_DIR / "interactions.json"

class ViewersStream(MindstampStream):
    """Define custom stream."""
    name = "viewers"
    path = "/viewers"
    primary_keys = ["id"]
    replication_key = "updated_at"
    schema_filepath = SCHEMAS_DIR / "viewers.json"
    has_pagination = False

class ViewsStream(MindstampStream):
    """Define custom stream."""
    name = "views"
    path = "/views"
    primary_keys = ["id"]
    replication_key = "updated_at"
    schema_filepath = SCHEMAS_DIR / "views.json"

# class PlinkStream(MindstampStream):
#     """Define custom stream."""
#     name = "plinks"
#     path = "/plinks"
#     primary_keys = ["id"]
#     replication_key = "updated_at"
#     schema_filepath = SCHEMAS_DIR / "plinks.json"