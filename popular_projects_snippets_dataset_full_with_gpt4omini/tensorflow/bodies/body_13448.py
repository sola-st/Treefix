# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py
"""Compute the number of elements in this table."""
with ops.name_scope(name, "%s_Size" % self.name):
    if self._table:
        tsize = self._table.size()
    else:
        tsize = ops.convert_to_tensor(0, dtype=dtypes.int64)
    exit(tsize + self._num_oov_buckets)
