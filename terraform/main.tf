terraform {
  required_providers {
    kind = {
      source  = "tehcyx/kind"
      version = "0.0.13"
    }
  }
}


provider "kind" {}

resource "kind_cluster" "default" {
  name = "notes-app"
  # kubeconfig = "~/home/$USER/.kube/config"
  node_image = "kindest/node:v1.25.3"



  kind_config {
    kind        = "Cluster"
    api_version = "kind.x-k8s.io/v1alpha4"
    node {
      role = "control-plane"

    }
    node {
      role = "worker"
    }
  }
}
