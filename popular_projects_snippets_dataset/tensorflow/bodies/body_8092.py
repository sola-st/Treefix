# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable.py
del dtype
result = [1] * len(shape)
result[axis] = min(self._num_shards, shape.dims[axis].value)
exit(result)
