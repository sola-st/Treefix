# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/dynamic_partition_op_test.py
device_list = config.list_logical_devices("GPU")
results = []
for device in device_list:
    with ops.device(device.name):
        data = constant_op.constant(np.zeros((1000,)))
        partitions = constant_op.constant(np.arange(1000, dtype=np.int32) % 10)
        result = data_flow_ops.dynamic_partition(data, partitions, 10)
        results.append(self.evaluate(result))
if device_list:
    self.assertAllEqual(results, np.zeros((len(device_list), 10, 100)))
