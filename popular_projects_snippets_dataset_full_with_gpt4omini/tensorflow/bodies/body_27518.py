# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/assert_cardinality_test.py
dataset = dataset_ops.Dataset.range(10).filter(lambda x: True)
self.assertEqual(
    self.evaluate(cardinality.cardinality(dataset)), cardinality.UNKNOWN)
self.assertDatasetProduces(dataset, expected_output=range(10))
dataset = dataset.apply(cardinality.assert_cardinality(10))
self.assertEqual(self.evaluate(cardinality.cardinality(dataset)), 10)
self.assertDatasetProduces(dataset, expected_output=range(10))
