# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
dataset = dataset_ops.Dataset.range(10 * x, 10 * x + 2)
dataset = self.make_distributed_dataset(
    dataset,
    cluster,
    data_transfer_protocol=self._get_data_transfer_protocol())
exit(dataset)
