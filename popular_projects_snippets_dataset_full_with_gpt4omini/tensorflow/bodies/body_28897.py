# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/get_single_element_test.py
dataset = dataset_ops.Dataset.from_tensors(42)
self.assertEqual(
    self.evaluate(dataset.get_single_element(name="get_single_element")),
    42)
