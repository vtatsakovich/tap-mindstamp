"""Mindstamp tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th

from tap_mindstamp.streams import (
    MindstampStream,
    VideosStream,
    InteractionsStream,
    ViewersStream,
    ViewsStream
)

STREAM_TYPES = [
    VideosStream,
    InteractionsStream,
    ViewersStream,
    ViewsStream
]

class TapMindstamp(Tap):
    """Mindstamp tap class."""
    name = "tap-mindstamp"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            description="The token to authenticate against the API service"
        ),
        th.Property(
            "api_url",
            th.StringType,
            default="https://api.mysample.com",
            description="The url for the API service"
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
