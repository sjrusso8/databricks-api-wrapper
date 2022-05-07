from .base import BaseWrapper


class ClustersAPI(BaseWrapper):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cluster_api_version = "2.0"
        self._cluster_create = f"{self.cluster_api_version}/clusters/create"
        self._cluster_edit = f"{self.cluster_api_version}/clusters/edit"
        self._cluster_start = f"{self.cluster_api_version}/clusters/start"
        self._cluster_restart = f"{self.cluster_api_version}/clusters/restart"
        self._cluster_resize = f"{self.cluster_api_version}/clusters/resize"
        self._cluster_delete = f"{self.cluster_api_version}/clusters/delete"
        self._cluster_permanent_delete = f"{self.cluster_api_version}/clusters/permanent-delete"
        self._cluster_get = f"{self.cluster_api_version}/clusters/get"
        self._cluster_pin = f"{self.cluster_api_version}/clusters/pin"
        self._cluster_unpin = f"{self.cluster_api_version}/clusters/unpin"
        self._cluster_list = f"{self.cluster_api_version}/clusters/list"
        self._cluster_node_type_list = f"{self.cluster_api_version}/clusters/list-node-types"
        self._spark_versions = f"{self.cluster_api_version}/clusters/spark-versions"
        self._cluster_events = f"{self.cluster_api_version}/clusters/events"

    def create_cluster(self, data):
        return self.request(method='POST', end_point=self._cluster_create, data=data)

    def edit_cluster(self, data):
        return self.request(method='POST', end_point=self._cluster_edit, data=data)

    def start_cluster(self, data):
        return self.request(method='POST', end_point=self._cluster_start, data=data)

    def restart_cluster(self, data):
        return self.request(method='POST', end_point=self._cluster_restart, data=data)

    def resize_cluster(self, data):
        return self.request(method='POST', end_point=self._cluster_resize, data=data)

    def delete_cluster(self, data):
        return self.request(method='POST', end_point=self._cluster_delete, data=data)

    def permanent_delete_cluster(self, data):
        return self.request(method='POST', end_point=self._cluster_permanent_delete, data=data)

    def get_cluster(self, data):
        return self.request(method='GET', end_point=self._cluster_get, data=data)

    def pin_cluster(self, data):
        return self.request(method='POST', end_point=self._cluster_pin, data=data)

    def unpin_cluster(self, data):
        return self.request(method='POST', end_point=self._cluster_unpin, data=data)

    def list_clusters(self):
        return self.request(method='GET', end_point=self._cluster_list)

    def list_cluster_node_types(self):
        return self.request(method='GET', end_point=self._cluster_node_type_list)

    def list_spark_versions(self):
        return self.request(method='GET', end_point=self._spark_versions)

    def cluster_events(self, data):
        return self.request(method='POST', end_point=self._spark_versions, data=data)
