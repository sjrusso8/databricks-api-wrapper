from .base import BaseWrapper


class TokenManagementAPI(BaseWrapper):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cluster_api_version = "2.0"
