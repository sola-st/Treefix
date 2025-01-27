# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_tensor_slices_test.py
dss = [dataset_ops.Dataset.range(10).map(
    lambda x: collections.OrderedDict([("x", x)])) for _ in range(10)]
ds = dataset_ops.Dataset.from_tensor_slices(dss)
ds = ds.flat_map(lambda x: x)
self.assertDatasetProduces(
    ds,
    expected_output=[collections.OrderedDict([("x", x)])
                     for x in list(range(10)) * 10])
