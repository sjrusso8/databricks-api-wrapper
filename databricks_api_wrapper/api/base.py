import json
import requests


class BaseWrapper(object):
    def __init__(self, **kwargs):
        self.host = kwargs.pop("host")
        self.token = kwargs.pop("token")
        self.uri = f"{self.host}/api/"
        self.headers = {"Authorization": f"Bearer {self.token}"}

    # will need to implement a validation checker if the host ends with a /

    def _get_uri_endpoint(self, end_point):
        url = self.uri + end_point

        return url

    def request(self, method, end_point, data=None):
        url = self._get_uri_endpoint(end_point=end_point)

        if data:
            data_json = json.dumps(data, ensure_ascii=False)
        else:
            data_json = None

        if method == 'GET':
            return requests.get(url=url, headers=self.headers, json=data_json)
        if method == 'POST':
            return requests.post(url=url, headers=self.headers, json=data_json)
        if method == 'PATCH':
            return requests.patch(url=url, headers=self.headers, json=data_json)
        if method == 'PUT':
            return requests.put(url=url, headers=self.headers, json=data_json)
