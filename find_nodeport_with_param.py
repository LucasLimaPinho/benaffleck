import kubernetes
from kubernetes import client, config
import urllib3
import sys
import json
# Number of nodePorts per pyspark notebook

num = 2

# Namespace

ns = 'argo'

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

config.load_incluster_config()
v1 = client.CoreV1Api()
available_ports = []
service_names = []
ips = []
ret = v1.list_namespaced_service(namespace="argo", label_selector="app=sant,available=true")
for i in ret.items[:num]:
    [available_ports.append(i.spec.ports[j].node_port) for j in range(len(i.spec.ports))]
if (len(available_ports) < num):
    print("There are no sufficient ports available for this workflow.")
    sys.exit(1)

res = {"containerPort": available_ports[0]}

print(json.dumps(res))