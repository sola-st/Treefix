# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device_test.py
if self.device_type != "CPU":
    self.skipTest("Iterator GetNext doesn't work on accelerators.")
datasets = [
    dataset_ops.Dataset.from_tensor_slices(
        [i + 1, (i + 1) * 2, (i + 1) * 3])
    for i in range(len(self.device.components))]
parallel_dataset = self.device.pack(datasets)
with self.device:
    iterator = iter(parallel_dataset)
    parallel_sample = next(iterator)
component_iterators = self.device.unpack(iterator)
self.assertEqual(2, next(component_iterators[0]).numpy())
self.assertEqual(1, self.device.unpack(parallel_sample)[0].numpy())
self.assertEqual(4, next(component_iterators[1]).numpy())
self.assertEqual(2, self.device.unpack(parallel_sample)[1].numpy())
