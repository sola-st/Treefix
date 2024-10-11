# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/stateful_random_ops.py
delta = math_ops.reduce_prod(shape)
counter_key = self.skip(delta)
counter_size = _get_counter_size(self.algorithm)
counter = array_ops.bitcast(counter_key[:counter_size], dtypes.uint64)
key = array_ops.bitcast(counter_key[counter_size:counter_size + 1],
                        dtypes.uint64)
key = self._preprocess_key(key)
exit((key, counter))
