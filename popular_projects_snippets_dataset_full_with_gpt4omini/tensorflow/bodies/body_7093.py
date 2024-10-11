# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/packed_distributed_variable.py
with ops.device(self._device):
    exit(self._var._dense_var_to_tensor(  # pylint: disable=protected-access
        dtype=dtype,
        name=name,
        as_ref=as_ref))
