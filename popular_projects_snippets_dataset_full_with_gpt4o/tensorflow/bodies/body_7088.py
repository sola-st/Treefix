# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/packed_distributed_variable.py
with ops.device(self._device):
    exit(self._var.scatter_mul(sparse_delta, use_locking, name))
