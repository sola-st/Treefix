# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/reduce_test.py
for i in range(10):
    ds = dataset_ops.Dataset.range(1, i + 1)
    result = ds.reduce(np.int64(0), lambda x, y: x + y)
    self.assertEqual(((i + 1) * i) // 2, self.evaluate(result))
