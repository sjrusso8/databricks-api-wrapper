from .base import BaseWrapper


class DBFSAPI(BaseWrapper):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cluster_api_version = "2.0"
        self._dbfs_add_block = f"{self.cluster_api_version}/dbfs/add-block"
        self._dbfs_close = f"{self.cluster_api_version}/dbfs/close"
        self._dbfs_create = f"{self.cluster_api_version}/dbfs/create"
        self._dbfs_delete = f"{self.cluster_api_version}/dbfs/delete"
        self._dbfs_get_status = f"{self.cluster_api_version}/dbfs/get-status"
        self._dbfs_list = f"{self.cluster_api_version}/dbfs/list"
        self._dbfs_mkdirs = f"{self.cluster_api_version}/dbfs/mkdirs"
        self._dbfs_move = f"{self.cluster_api_version}/dbfs/move"
        self._dbfs_put = f"{self.cluster_api_version}/dbfs/put"
        self._dbfs_read = f"{self.cluster_api_version}/dbfs/read"

    def dbfs_add_block(self, data):
        return self.request(method="POST", end_point=self._dbfs_add_block, data=data)

    def dbfs_close(self, data):
        return self.request(method="POST", end_point=self._dbfs_close, data=data)

    def dbfs_create(self, data):
        return self.request(method="POST", end_point=self._dbfs_create, data=data)

    def dbfs_delete(self, data):
        return self.request(method="POST", end_point=self._dbfs_delete, data=data)

    def dbfs_get_status(self, data):
        return self.request(method="GET", end_point=self._dbfs_get_status, data=data)

    def dbfs_list(self, data):
        return self.request(method="GET", end_point=self._dbfs_list, data=data)

    def dbfs_mkdirs(self, data):
        return self.request(method="POST", end_point=self._dbfs_mkdirs, data=data)

    def dbfs_move(self, data):
        return self.request(method="POST", end_point=self._dbfs_move, data=data)

    def dbfs_put(self, data):
        return self.request(method="POST", end_point=self._dbfs_put, data=data)

    def dbfs_read(self, data):
        return self.request(method="GET", end_point=self._dbfs_read, data=data)
