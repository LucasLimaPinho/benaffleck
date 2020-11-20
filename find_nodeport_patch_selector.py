import kubernetes
from kubernetes import client, config
import urllib3
import sys
import json

# Number of nodePorts per pyspark notebook
num = 2

# Namespace
ns = 'argo'

# Random user
user = 'x247451'

# Body message to patch services
def get_body(user,svcname):
    body = {
        "metadata": {
            "labels": {
                "available": "false",
                "app": "sant",
                "user": user,
                "svcname": svcname
            }
        },
        "spec": {
            "selector":{
                "user": user
            }
        }
    }

    return body

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

config.load_incluster_config()
v1 = client.CoreV1Api()
services = []
nodeports = []
svc_list = v1.list_namespaced_service(namespace="argo", label_selector="app=sant,available=true")
if (len(svc_list.items) < num):
    logger.error("There are not enough nodeports to run this workflow.")
else:
    for np in svc_list.items[:num]:
        v1.patch_namespaced_service(np.metadata.name, ns, get_body(user,np.metadata.name))
        services.append(np.metadata.name)
        [nodeports.append(np.spec.ports[j].node_port) for j in range(len(np.spec.ports))]
with open("/tmp/svcname1.txt","w") as f:
    f.write(services[0])
    f.close()
with open("/tmp/svcname2.txt","w") as f:
    f.write(services[1])
    f.close()
with open("/tmp/nodeport1.txt","w") as f:
    f.write(nodeports[0])
    f.close()
with open("/tmp/nodeport2.txt","w") as f:
    f.write(nodeports[1])
    f.close()

print(f"Services allocated: {services}")
print(f"Nodeports allocated: {nodeports}")
print(svc_list) 
