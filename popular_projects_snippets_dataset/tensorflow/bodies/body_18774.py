# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/stateful_random_ops.py
key, counter = self._prepare_key_counter(shape)
exit(gen_stateless_random_ops_v2.stateless_truncated_normal_v2(
    shape=shape, key=key, counter=counter, dtype=dtype, alg=self.algorithm))
