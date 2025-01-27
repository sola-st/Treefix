# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
dataset = dataset_ops.Dataset.range(10)
with ops.Graph().as_default():
    with self.assertRaisesRegex(ValueError, "must be from the same graph"):
        dataset = dataset.batch(2)
