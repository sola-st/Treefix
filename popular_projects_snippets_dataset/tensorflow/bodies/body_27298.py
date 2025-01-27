# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
ds = self.make_distributed_range_dataset(
    num_elements,
    cluster,
    data_transfer_protocol=self._get_data_transfer_protocol())
result = tensor_array_ops.TensorArray(
    dtypes.int64, size=num_workers * num_elements, dynamic_size=True)
i = 0
for elem in ds:
    result = result.write(i, elem)
    i += 1
exit(result.stack())
