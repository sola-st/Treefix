# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/padded_batch_test.py
ds = dataset_ops.Dataset.range(5)
ds = ds.map(lambda x: math_ops.cast(x, dtypes.bfloat16))
ds = ds.padded_batch(10)
self.assertDatasetProduces(
    ds, expected_output=[[0.0, 1.0, 2.0, 3.0, 4.0]])
