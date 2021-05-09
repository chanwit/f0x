# The f0x project
Running Flux effortlessly anywhere

## Implementations

### Rootless Flux

Rootless Flux is a F0x implementation deployed as a StatefulSet along with a side-car K8s API server. 
This similar technique has been used recently in other virtual K8s cluster implementations, such as KCP and vcluster. 
But Rootless Flux's controlplane is optimized just to run Flux.

#### Why Rootless Flux is important?

In corporate Kubernetes clusters, users normally are allowed to use their namespaces with limited access. No ClusterAdmin. No CRDs are allowed.
Rootless Flux solves this problem by offering a rootless Flux controlplane, which is able to run in those limited namespaces without requiring ClusterAdmin nor CRDs installed on the host cluster. The controlplane is pre-loaded CRDs and other resources for Flux.

Rootless Flux allows GitOps to run anywhere even in a restricted cluster environment, like OpenShift Dev Sandbox.  

### Flux for Docker

F0x in this mode runs GitOps Toolkit components in Docker containers without requiring a Kubernetes cluster. F0x uses only the API and `etcd` servers to help GOTK components talk to each others. The current implementation uses Docker-Compose to up and running F0x with a simple Docker bridge network. Current F0x supports running Source Controller and Kustomization Controller only.

To make F0x useable, we require a usecase-specific controller and CRDs. See example.

## Use cases

F0x could be applied for:
  - Rootless Flux - running F0x as an independent Flux cluster inside a restricted Kubernete namespace
  - Edge-computing use cases
  - Standalone GitOps applications
  - etc.

## Limitation
  - No pod deployment and we don't have any Kubernetes node in this implementation
