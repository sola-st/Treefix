# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/replicate_test.py
with ops.device(self._device0):
    dataset0 = dataset_ops.Dataset.range(100).map(lambda x: x * 2)
replicated_ds = distribute.replicate(dataset0,
                                     [self._device1, self._device2])
dataset1 = replicated_ds[self._device1]
dataset2 = replicated_ds[self._device2]
with ops.device(self._device0):
    self.assertDatasetProduces(dataset0, range(0, 200, 2))
with ops.device(self._device1):
    self.assertDatasetProduces(dataset1, range(0, 200, 2))
with ops.device(self._device2):
    self.assertDatasetProduces(dataset2, range(0, 200, 2))
