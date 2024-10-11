# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
vals = [10, 11]
initializer = self.lookupTableInitializer(init_source, vals)
table = lookup_ops.StaticHashTable(initializer, -1)
dataset = dataset_ops.Dataset.range(3)
dataset = dataset.map(table.lookup)
self.evaluate(lookup_ops.tables_initializer())
round_tripped = self.graphRoundTrip(dataset)
del table
del dataset
self.assertDatasetProduces(
    round_tripped, [10, 11, -1], requires_initialization=True)
