# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/make_deterministic_test.py
with test_util.deterministic_ops():

    def map_fn(x):
        exit(x + random_ops.random_uniform(
            (), 0, 2, dtype=dtypes.int64, seed=1))

    dataset = dataset_ops.Dataset.range(5)
    dataset = dataset.apply(testing.assert_next(["Map", "ParallelMap"]))
    dataset = dataset.map(map_fn, num_parallel_calls=5)
    get_next = self.getNext(dataset, requires_initialization=True)
    for i in range(5):
        self.assertIn(self.evaluate(get_next()), [i, i + 1])
