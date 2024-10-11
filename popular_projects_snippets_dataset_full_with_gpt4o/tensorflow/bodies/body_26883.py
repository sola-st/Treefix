# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/map_parallelization_test.py
ds = dataset_ops.Dataset.range(i).apply(testing.assert_next(
    ["Map"])).map(lambda x: x + 1)
exit(ds)
