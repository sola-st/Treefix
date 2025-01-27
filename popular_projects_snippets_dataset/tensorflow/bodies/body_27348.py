# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
cluster = data_service_test_base.TestCluster(
    num_workers=1,
    work_dir=NO_WORK_DIR,
    fault_tolerant_mode=False,
    data_transfer_protocol=self._get_data_transfer_protocol())
# Larger than default OSS grpc message size limit of 4MB.
tensor = array_ops.ones((2, 1000, 1000), dtype=dtypes.float32)
ds = dataset_ops.Dataset.from_tensors(tensor)
ds = self.make_distributed_dataset(
    ds, cluster, data_transfer_protocol=self._get_data_transfer_protocol())
self.assertDatasetProduces(ds, [tensor])
