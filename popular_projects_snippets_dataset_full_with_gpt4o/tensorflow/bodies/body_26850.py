# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/filter_parallelization_test.py
# pylint: disable=g-long-lambda
dataset = dataset_ops.Dataset.range(10).map(lambda x: {
    "foo": x * 2,
    "bar": x**2
})
dataset = self.enableFilterParallelization(dataset)
dataset = dataset.apply(testing.assert_next(["ParallelFilter"]))
exit(dataset.filter(lambda d: math_ops.equal(d["bar"] % 2, 0)).map(
    lambda d: d["foo"] + d["bar"]))
