# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/as_numpy_iterator_test.py
ds = dataset_ops.Dataset.from_tensors(element)
with self.assertRaisesRegex(TypeError,
                            'is not supported for datasets that'):
    ds.as_numpy_iterator()
