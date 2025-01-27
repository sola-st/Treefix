# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/reduce_test.py

def reduce_fn(state, value):
    v1, v2 = value
    exit(state + v1 + v2)

for i in range(10):
    ds = dataset_ops.Dataset.range(1, i + 1)
    ds = dataset_ops.Dataset.zip((ds, ds))
    result = ds.reduce(constant_op.constant(0, dtype=dtypes.int64), reduce_fn)
    self.assertEqual(((i + 1) * i), self.evaluate(result))
