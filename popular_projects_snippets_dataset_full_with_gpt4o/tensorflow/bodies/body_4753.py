# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy.py
if cluster_resolver and cluster_resolver.cluster_spec():
    self._initialize_multi_worker(cluster_resolver)
else:
    self._initialize_local(
        compute_devices, parameter_device, cluster_resolver=cluster_resolver)
