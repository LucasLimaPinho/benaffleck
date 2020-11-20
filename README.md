# Kubernetes - Service Discovery

Kubernetes is a very dynamic system. The system is involved in placing Pods on nodes, making sure they are up & running, and rescheduling them as needed. While the dynamic nature of Kubernetes makes it easy to run a lot of things, it creates problems when it comes to finding those things. 

Service-Discvoery tools help solve the problem of finding which processes are listening at which addresses for which services. A Service Object is a way to create a named label selector.

Oftentimes, the IPs for Pods are only reachable from within the cluster. The most portable way to do this is to use a feature called NodePorts, which enhance a service even further. In addition to a cluster IP, the system picks a port (or the user can specify one) and every node in the cluster then forwards traffic to that port to the service.

With this feature, if you can reach any node in the cluster you can contact a service. You use the NodePort without knowing where any of the Pods for that service are running. 


# Config Maps & Secrets

It is a good practice to make container images as reusable as possible. The same image should be able to be used for development, staging and production. It is even better if the same image is general-purpose enough to be used across applications and services. Testing and versioning get riskier and more complicated if images need to be recreated for each new environment. **But then how do we specialize the use of that image at runtime?**

This is where ConfigMaps and Secrets come into play. ConfigMaps are used to provide configuration information for workloads. This can either be fine-grained information (a short thing) or a composite value in the form of a file. 

Secrets are similar to ConfigMaps, but focused on making senstitive information available to the workload. They can be ised for things like credentials or TLS certificates.

# Config Maps

One way to think of a ConfigMap is a Kubernetes object that defines a small filesystem. Another way is as a set of variables that can be used when defining the environment or command line for your containers. The key thing is that the ConfigMap is combined with the Pod righ before it is run. This means that the container image and the Pod definition itself can be reused across many apps by just changing the ConfigMap that is used.


The ConfigMap is really just some key/value pairs stored in a object. The interesting stuff happens when you try to use a ConfigMap.

There are three main ways to use a ConfigMap:

1. FileSystem

You can mount a ConfigMap into a Pod. A file is created for each entry based on the key name. The contents of that faile are set to the value.

2. Environment Variable

A ConfigMao can be used to dynamically set the value of an environment variable.

3. Command-line argument

Kubernetes supports dynamicallly creating the command line for a container based on a ConfigMap values.

