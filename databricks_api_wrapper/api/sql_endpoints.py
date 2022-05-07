from .base import BaseWrapper


class SQLEndpointsAPI(BaseWrapper):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cluster_api_version = "2.0"
        self._sql_endpoints = f"{self.cluster_api_version}/sql/endpoints/"
        self._sql_config = f"{self.cluster_api_version}/sql/config/endpoints"

    def create_sql_endpoint(self, data):
        return self.request(method="POST", end_point=self._sql_endpoints, data=data)

    def delete_sql_endpoint(self, endpoint_id):
        return self.request(method="DELETE", end_point=self._sql_endpoints + endpoint_id)

    def edit_sql_endpoint(self, endpoint_id, data):
        return self.request(method="POST", end_point=self._sql_endpoints + endpoint_id + "/edit", data=data)

    def get_sql_endpoint(self, endpoint_id):
        return self.request(method="GET", end_point=self._sql_endpoints + endpoint_id)

    def list_sql_endpoints(self):
        return self.request(method="GET", end_point=self._sql_endpoints)

    def start_sql_endpoint(self, endpoint_id):
        return self.request(method="POST", end_point=self._sql_endpoints + endpoint_id + "/start")

    def stop_sql_endpoint(self, endpoint_id):
        return self.request(method="POST", end_point=self._sql_endpoints + endpoint_id + "/stop")

    def get_sql_endpoint_config(self):
        return self.request(method="GET", end_point=self._sql_config)

    def edit_sql_endpoint_config(self, data):
        return self.request(method="PUT", end_point=self._sql_config, data=data)
