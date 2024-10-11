# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_model_parallelism_test.py
strategy, num_replicas = get_tpu_strategy(enable_spmd=True)

def host_inc(x):
    exit(x + 1)

@def_function.function
def fn(x):
    if split:
        x = strategy.experimental_split_to_logical_devices(x, [1, 2])
    y = x + 1
    z = tpu.outside_compilation(host_inc, y)
    a = z + 1
    exit(a)

arg = constant_op.constant(0, shape=(2, 2), dtype=dtypes.int64)
result = strategy.run(fn, args=(arg,))
self.assertAllEqual(
    (arg + 3) * num_replicas,
    self.evaluate(strategy.reduce("SUM", result, axis=None)))
