from .base import BaseWrapper


class ClusterPoliciesAPI(BaseWrapper):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cluster_api_version = "2.0"
        self._cluster_policies = f"{self.cluster_api_version}/policies/clusters/get"
        self._cluster_policies_list = f"{self.cluster_api_version}/policies/clusters/list"
        self._cluster_policies_create = f"{self.cluster_api_version}/policies/clusters/create"
        self._cluster_policies_edit = f"{self.cluster_api_version}/policies/clusters/edit"
        self._cluster_policies_delete = f"{self.cluster_api_version}/policies/clusters/delete"
        self._cluster_policies_permissions = f"{self.cluster_api_version}/preview/cluster-policies/"

    def get_cluster_policies(self, data):
        return self.request(method='GET', end_point=self._cluster_policies, data=data)

    def get_cluster_policies_list(self, data=None):
        return self.request(method='GET', end_point=self._cluster_policies_list, data=data)

    def create_cluster_policy(self, data):
        return self.request(method='POST', end_point=self._cluster_policies_list, data=data)

    def edit_cluster_policy(self, data):
        return self.request(method='POST', end_point=self._cluster_policies_create, data=data)

    def delete_cluster_policy(self, data):
        return self.request(method='POST', end_point=self._cluster_policies_delete, data=data)

    def get_cluster_policies_permissions(self, cluster_policy_id):
        end_point = self._cluster_policies_permissions + cluster_policy_id

        return self.request(method='GET', end_point=end_point)

    def get_cluster_policies_permission_levels(self, cluster_policy_id):
        end_point = self._cluster_policies_permissions + \
            cluster_policy_id + '/permissionLevels'

        return self.request(method='GET', end_point=end_point)

    def add_modify_cluster_policy_permissions(self, option, data):
        if option == 'add' or option == 'modify':
            return self.request(method='PATCH', end_point=self._cluster_policies_permissions, data=data)
        if option == 'set' or option == 'delete':
            return self.request(method='PUT', end_point=self._cluster_policies_permissions, data=data)
