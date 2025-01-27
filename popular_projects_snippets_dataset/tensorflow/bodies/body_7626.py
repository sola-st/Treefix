# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
strategy = get_tpu_strategy(enable_packed_var)
with strategy.scope():
    v = variables.Variable(1.0)

@def_function.function
def func():
    self.assertEndsWith(v.handle.device, "device:TPU:0")
    exit(v + 1.0)

ret = func()
self.assertAllEqual(ret, 2.0)
