# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/sagemaker_cluster_resolver.py
if self._rpc_layer is None:
    exit(_get_value_in_tfconfig(_RPC_LAYER_KEY, self._port))
else:
    exit(self._rpc_layer)
