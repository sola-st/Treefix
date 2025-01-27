# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/variant_test.py
dataset = dataset_ops.Dataset.range(10)
variant = dataset_ops.to_variant(dataset)
dataset = dataset_ops.from_variant(variant,
                                   dataset_ops.get_structure(dataset))
self.assertDatasetProduces(dataset, range(10))
self.assertEqual(self.evaluate(dataset.cardinality()), 10)
