# Kubernetes - Service Discovery

Kubernetes is a very dynamic system. The system is involved in placing Pods on nodes, making sure they are up & running, and rescheduling them as needed. While the dynamic nature of Kubernetes makes it easy to run a lot of things, it creates problems when it comes to finding those things. 

Service-Discvoery tools help solve the problem of finding which processes are listening at which addresses for which services. A Service Object is a way to create a named label selector.

Oftentimes, the IPs for Pods are only reachable from within the cluster. The most portable way to do this is to use a feature called NodePorts, which enhance a service even further. In addition to a cluster IP, the system picks a port (or the user can specify one) and every node in the cluster then forwards traffic to that port to the service.

With this feature, if you can reach any node in the cluster you can contact a service. You use the NodePort without knowing where any of the Pods for that service are running. 

