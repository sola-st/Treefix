# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/filter_parallelization_test.py
dataset = dataset_ops.Dataset.range(10).map(
    lambda x: {"foo": x * 2, "bar": x**2})
dataset = self.enableFilterParallelization(dataset)
dataset = dataset.apply(testing.assert_next(["ParallelFilter"]))
dataset = apply_filter(dataset, lambda d: math_ops.equal(d["bar"] % 2, 0))
dataset = dataset.map(lambda d: d["foo"] + d["bar"])
self.assertDatasetProduces(
    dataset,
    expected_output=[(i * 2 + i**2) for i in range(10) if not (i**2) % 2])
