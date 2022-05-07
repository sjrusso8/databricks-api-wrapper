from fastapi import APIRouter

from databricks_api_wrapper.api.utils import databricks_confg
from databricks_api_wrapper.api.clusters import ClustersAPI

router = APIRouter()

dbrcfg = databricks_confg()
cluster_api = ClustersAPI(**dbrcfg)


@router.get("/clusters/")
def list_clusters():
    return cluster_api.get_cluster_list().json()
