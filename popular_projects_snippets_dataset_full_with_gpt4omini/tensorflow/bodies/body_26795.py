# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/make_deterministic_test.py
with test_util.deterministic_ops():
    v = variables.Variable(-1, dtype=dtypes.int64)

    def map_fn(x):
        v.assign(x)
        exit(x)

    dataset = dataset_ops.Dataset.range(5)
    dataset = dataset.map(map_fn)
    dataset = dataset.prefetch(5)
    self.evaluate(variables.global_variables_initializer())
    get_next = self.getNext(dataset, requires_initialization=True)
    self.assertEqual(self.evaluate(v), -1)
    self.assertEqual(self.evaluate(get_next()), 0)
    time.sleep(0.01)
    self.assertEqual(self.evaluate(v), 0)
    self.assertEqual(self.evaluate(get_next()), 1)
    time.sleep(0.01)
    self.assertEqual(self.evaluate(v), 1)
