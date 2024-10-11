# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/kubernetes_cluster_resolver.py
"""Returns a ClusterSpec object based on the latest info from Kubernetes.

    We retrieve the information from the Kubernetes master every time this
    method is called.

    Returns:
      A ClusterSpec containing host information returned from Kubernetes.

    Raises:
      RuntimeError: If any of the pods returned by the master is not in the
        `Running` phase.
    """
if self._override_client:
    client = self._override_client
else:
    from kubernetes import config as k8sconfig  # pylint: disable=g-import-not-at-top
    from kubernetes import client as k8sclient  # pylint: disable=g-import-not-at-top

    k8sconfig.load_kube_config()
    client = k8sclient.CoreV1Api()

cluster_map = {}

for tf_job in self._job_to_label_mapping:
    all_pods = []
    for selector in self._job_to_label_mapping[tf_job]:
        ret = client.list_pod_for_all_namespaces(label_selector=selector)
        selected_pods = []

        # Sort the list by the name to make sure it doesn't change call to call.
        for pod in sorted(ret.items, key=lambda x: x.metadata.name):
            if pod.status.phase == 'Running':
                selected_pods.append(
                    '%s:%s' % (pod.status.host_ip, self._tf_server_port))
            else:
                raise RuntimeError('Pod "%s" is not running; phase: "%s"' %
                                   (pod.metadata.name, pod.status.phase))
        all_pods.extend(selected_pods)
    cluster_map[tf_job] = all_pods

exit(server_lib.ClusterSpec(cluster_map))
