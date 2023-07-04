"""REST client handling, including MindstampStream base class."""

from pathlib import Path
from typing import Any, Dict, Optional

import singer
import requests
from singer_sdk.authenticators import BearerTokenAuthenticator
from singer_sdk.streams import RESTStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")
LOGGER = singer.get_logger()


class MindstampStream(RESTStream):
    """Mindstamp stream class."""

    # _LOG_REQUEST_METRIC_URLS = True

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        return self.config["api_url"]

    records_jsonpath = "$[*]"
    has_pagination = True
    limit = 100 if has_pagination else None

    @property
    def authenticator(self) -> BearerTokenAuthenticator:
        """Return a new authenticator object."""
        return BearerTokenAuthenticator.create_for_stream(
            self,
            token=self.config.get("api_key")
        )

    def get_next_page_token(
            self, response: requests.Response, previous_token: Optional[Any]
    ) -> Optional[Any]:
        """Return a token for identifying next page or None if no more pages."""
        if response is None:
            return None

        data = response.json()

        if not data:
            return None

        if self.has_pagination:
            previous_token = previous_token or 0

            return previous_token + self.limit

        return None

    def get_url_params(
            self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        params: dict = {}
        if self.has_pagination:
            params["limit"] = self.limit
        if next_page_token:
            params["offset"] = next_page_token

        LOGGER.info('Applied params: ')
        LOGGER.info(params)

        return params
