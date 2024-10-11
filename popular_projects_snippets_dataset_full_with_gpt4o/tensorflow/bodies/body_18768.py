# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/stateful_random_ops.py
resource_variable_ops.variable_accessed(var)
# TODO(wangpeng): Cache the cast algorithm instead of casting everytime.
exit(gen_stateful_random_ops.rng_read_and_skip(
    var.handle,
    alg=math_ops.cast(self.algorithm, dtypes.int32),
    delta=math_ops.cast(delta, dtypes.uint64)))
