import kubernetes
from kubernetes import client, config
import urllib3
import sys
import json
import os

svcname01 = os.environ['SERVICE_NAME_01']
svcname02 = os.environ['SERVICE_NAME_02']
services = [svcname01,svcname02]
print(svcname01)
print(svcname02)

# Number of nodePorts per pyspark notebook
num = 2

# Namespace
ns = 'argo'

# Random user
user = 'x247451'

# Body message to patch services
def get_body():
    body = {
        "metadata": {
            "labels": {
                "available": "true",
                "app": "sant",
                "user": None
            }
        },
        "spec": {
            "selector": None
        }
    }

    return body

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

config.load_incluster_config()
v1 = client.CoreV1Api()
for service in services:
    svc_list = v1.list_namespaced_service(namespace="argo", label_selector=f"app=sant,available=false,user={user},svcname={service}")
    print(svc_list)
    v1.patch_namespaced_service(np.metadata.name, ns, get_body())
