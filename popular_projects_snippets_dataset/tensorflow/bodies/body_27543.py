# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/replicate_test.py
with ops.device(self._device0):
    counter_var = variable_scope.get_variable(
        "counter", (), dtypes.int32, use_resource=True)
    dataset0 = dataset_ops.Dataset.range(100).map(
        lambda _: counter_var.assign_add(1))
replicated_ds = distribute.replicate(dataset0,
                                     [self._device1, self._device2])
dataset1 = replicated_ds[self._device1]
dataset2 = replicated_ds[self._device2]
self.evaluate(counter_var.initializer)
with ops.device(self._device1):
    self.assertDatasetProduces(
        dataset1, range(1, 101), requires_initialization=True)
with ops.device(self._device2):
    self.assertDatasetProduces(
        dataset2, range(1, 101), requires_initialization=True)
# Iterate through the original device last so that replication happens
# before counter_var is modified. The order only matters in graph mode.
with ops.device(self._device0):
    self.assertDatasetProduces(
        dataset0, range(1, 101), requires_initialization=True)
