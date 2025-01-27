# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/filter_test.py
dataset = dataset_ops.Dataset.range(10).map(
    lambda x: {"foo": x * 2, "bar": x**2})
dataset = apply_filter(dataset, lambda d: math_ops.equal(d["bar"] % 2, 0))
dataset = dataset.map(lambda d: d["foo"] + d["bar"])
self.assertDatasetProduces(
    dataset,
    expected_output=[(i * 2 + i**2) for i in range(10) if not (i**2) % 2])
