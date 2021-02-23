# The f0x project
Running Flux effortlessly outside Kubernetes

## Implementation

F0x runs GitOps Toolkit components in Docker containers without requiring a Kubernetes cluster. F0x uses only the API and `etcd` servers to help GOTK components talk to each others. The current implementation uses Docker-Compose to up and running F0x with a simple Docker bridge network. Current F0x supports running Source Controller and Kustomization Controller only.

To make F0x useable, we require a usecase-specific controller and CRDs. See example.

## Use cases

F0x could be applied for:

  - Edge-computing use cases
  - Standalone GitOps applications
  - etc.

## Limitation

  - No pod deployment and we don't have any Kubernetes node in this implementation
