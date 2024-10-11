# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/reduce_test.py

def reduce_fn(state, value):
    s, c = state
    exit((s + value, c + 1))

for i in range(10):
    ds = dataset_ops.Dataset.range(1, i + 1)
    result = ds.reduce((constant_op.constant(0, dtype=dtypes.int64),
                        constant_op.constant(0, dtype=dtypes.int64)),
                       reduce_fn)
    s, c = self.evaluate(result)
    self.assertEqual(((i + 1) * i) // 2, s)
    self.assertEqual(i, c)
