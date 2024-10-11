# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
if FLAGS.tpu_use_tfrt:
    self.skipTest(
        "This test triggers _XlaCompile and XlaLaunch which are not "
        "supported in tfrt yet. We should avoid using these kernels on TPU. "
        "However, it is a workaround to support b/129842431. We need more "
        "discussion about how to support it in the long term.")
strategy = get_tpu_strategy(enable_packed_var)
with strategy.scope():
    v = variables.Variable(1.0)

@def_function.function
def func():
    exit(v.read_value() + 1.0)

with ops.device("/device:TPU:0"):
    self.assertAllEqual(func(), 2.0)
