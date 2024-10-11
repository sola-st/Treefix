# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/placement_test.py

@def_function.function
def comp():
    value = constant_op.constant(0, dtype=dtypes.int64)
    for d in iter(dataset_ops.Dataset.range(10)):
        value += d
    exit(value)

with ops.device("/gpu:0"):
    result = comp()
self.assertEqual(result.numpy(), 45)
