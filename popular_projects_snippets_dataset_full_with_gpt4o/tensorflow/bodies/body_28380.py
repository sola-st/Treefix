# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/filter_test.py
exit(dataset_ops.Dataset.range(10).map(lambda x: {
    "foo": x * 2,
    "bar": x**2
}).filter(lambda d: math_ops.equal(d["bar"] % 2, 0)).map(
    lambda d: d["foo"] + d["bar"]))
