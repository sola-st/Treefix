# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/variant_test.py
dataset = dataset_ops.Dataset.range(10).map(lambda x: x * x)
variant = dataset_ops.to_variant(dataset)
dataset = dataset_ops.from_variant(variant,
                                   dataset_ops.get_structure(dataset))
self.assertDatasetProduces(dataset, [x * x for x in range(10)])
self.assertEqual(self.evaluate(dataset.cardinality()), 10)
