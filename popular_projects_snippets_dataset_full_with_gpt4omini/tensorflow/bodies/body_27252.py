# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/fault_tolerance_test.py
cluster = data_service_test_base.TestCluster(
    num_workers=0, work_dir=work_dir, fault_tolerant_mode=False)
# Larger than default OSS grpc message size limit of 4MB.
tensor = array_ops.ones((2, 1000, 1000), dtype=dtypes.float32)
ds = dataset_ops.Dataset.from_tensors(tensor)
ds = self.make_distributed_dataset(ds, cluster)
it = iter(ds)
cluster.add_worker()
self.assertAllEqual(next(it), tensor)
