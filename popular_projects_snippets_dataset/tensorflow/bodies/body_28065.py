# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/padded_batch_test.py
with self.assertRaisesRegex(ValueError, r'`padded_shapes`.*unknown rank'):
    ds = dataset_ops.Dataset.from_generator(
        lambda: iter([1, 2, 3]), output_types=dtypes.int32)
    ds.padded_batch(2)
