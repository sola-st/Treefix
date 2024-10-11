# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/unbatch_test.py
data = dataset_ops.Dataset.from_tensors((np.arange(7), np.arange(8),
                                         np.arange(9)))
with self.assertRaises(ValueError):
    data.unbatch()
