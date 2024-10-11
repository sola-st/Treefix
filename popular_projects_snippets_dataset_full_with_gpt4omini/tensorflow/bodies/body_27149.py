# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/multi_device_test.py
cluster = data_service_test_base.TestCluster(num_workers=1)
with ops.device(self._devices[0]):
    initializer = self.lookupTableInitializer("keyvaluetensor", [10, 11])
    table = lookup_ops.StaticHashTable(initializer, -1)
    self.evaluate(lookup_ops.tables_initializer())
    dataset = dataset_ops.Dataset.range(3)
    dataset = dataset.map(table.lookup)
    dataset = self.make_distributed_dataset(dataset, cluster)
    self.assertDatasetProduces(
        dataset, [10, 11, -1], requires_initialization=True)

with ops.device(self._devices[1]):
    dataset = dataset_ops.Dataset.range(3)
    dataset = dataset.map(table.lookup)
    with self.assertRaisesRegex(
        errors.FailedPreconditionError,
        "Serialization error while trying to register a dataset"):
        dataset = self.make_distributed_dataset(dataset, cluster)
        self.getDatasetOutput(dataset, requires_initialization=True)
