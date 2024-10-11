# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/reduce_test.py
dataset = dataset_ops.Dataset.from_tensors(42)
self.assertEqual(
    self.evaluate(
        dataset.reduce(0, lambda state, value: value, name="reduce")), 42)
