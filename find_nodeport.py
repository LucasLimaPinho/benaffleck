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
    service_names.append(i.metadata.name)
    ips.append(i.spec.cluster_ip)
    [available_ports.append(i.spec.ports[j].node_port) for j in range(len(i.spec.ports))]
if (len(available_ports) < num):
    print("There are no sufficient ports available for this workflow.")
    sys.exit(1)

with open("/tmp/nodeport1.txt", "w") as f:
    f.write(str(available_ports[0]))
    f.close()
with open("/tmp/nodeport2.txt", "w") as f:
    f.write(str(available_ports[1]))
    f.close()
with open("/tmp/servicehost1.txt", "w") as f:
    f.write(str(service_names[0].upper().replace("-","_") + "_SERVICE_HOST"))
    f.close()
with open("/tmp/servicehost2.txt", "w") as f:
    f.write(str(service_names[1].upper().replace("-","_") + "_SERVICE_HOST"))
    f.close()
with open("/tmp/serviceport1.txt", "w") as f:
    f.write(str(service_names[0].upper().replace("-","_") + "_SERVICE_PORT"))
    f.close()
with open("/tmp/serviceport2.txt", "w") as f:
    f.write(str(service_names[1].upper().replace("-","_") + "_SERVICE_PORT"))
    f.close()
with open("/tmp/ip1.txt","w") as f:
    f.write(str(ips[0]))
    f.close()
with open("/tmp/ip2.txt","w") as f:
    f.write(str(ips[1]))
    f.close()

print(available_ports[0])
print(available_ports[1])
print(service_names[0])
print(service_names[1])
print(ips[0])
print(ips[1])