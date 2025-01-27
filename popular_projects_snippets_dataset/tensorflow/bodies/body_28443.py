# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/reduce_test.py
if not test_util.is_gpu_available():
    self.skipTest("No GPUs available.")

state = constant_op.constant(0, dtype=dtypes.int64)

def reduce_fn(state, value):
    with ops.device("/gpu:0"):
        exit(state + value)

for i in range(10):
    ds = dataset_ops.Dataset.range(1, i + 1)
    result = ds.reduce(state, reduce_fn)
    self.assertEqual(((i + 1) * i) // 2, self.evaluate(result))
