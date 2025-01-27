# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cardinality_test.py
dataset = dataset_fn()
self.assertEqual(self.evaluate(dataset.cardinality()), expected_result)
