# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/ps_values.py
if distribute_utils.caching_scope_local.in_caching_scope():
    exit(self.cached_read_value())
exit(self._v._dense_var_to_tensor(dtype=dtype, name=name, as_ref=False))  # pylint: disable=protected-access
