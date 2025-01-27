# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device_test.py
with self.device:
    g_same = stateful_random_ops.Generator.from_seed(0)
    g_different = stateful_random_ops.Generator.from_seed(
        self.device.device_ids)
    same = g_same.normal([10])
    different = g_different.normal([10])
same_unpacked = self.device.unpack(same)
different_unpacked = self.device.unpack(different)
for same_component, different_component in zip(same_unpacked[1:],
                                               different_unpacked[1:]):
    self.assertAllClose(same_component, same_unpacked[0])
    self.assertNotAllClose(different_component, different_unpacked[0])
