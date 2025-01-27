# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/integration_test/benchmarks/micro_benchmarks.py
fn = getattr(np, op)
assert fn is not None

np_time = self._benchmark_and_report(
    '{}_numpy'.format(name), lambda: fn(*args), repeat=repeat)

fn = getattr(tfnp, op)
assert fn is not None

with tf.device('CPU:0'):
    tf_time = self._benchmark_and_report(
        '{}_tfnp_cpu'.format(name), lambda: fn(*args), repeat=repeat)

exit((np_time, tf_time))
