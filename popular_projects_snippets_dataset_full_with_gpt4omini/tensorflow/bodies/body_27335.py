# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
cluster = data_service_test_base.TestCluster(
    num_workers=1,
    data_transfer_protocol=self._get_data_transfer_protocol())

num_elements = 10
ds = dataset_ops.Dataset.range(num_elements)
dataset_id = data_service_ops.register_dataset(
    cluster.dispatcher_address(), ds, compression=self._get_compression())
wrong_spec = tensor_spec.TensorSpec(shape=(), dtype=dtypes.variant)
from_dataset_id_ds = data_service_ops.from_dataset_id(
    "parallel_epochs",
    cluster.dispatcher.target,
    dataset_id,
    wrong_spec,
    data_transfer_protocol=self._get_data_transfer_protocol())

with self.assertRaises(Exception):
    self.evaluate(self.getNext(from_dataset_id_ds)())
