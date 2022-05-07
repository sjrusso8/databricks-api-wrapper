from .base import BaseWrapper


class GroupsAPI(BaseWrapper):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cluster_api_version = "2.0"
