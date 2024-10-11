# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/snapshot_ft_test.py
ds = dataset_ops.Dataset.range(10)
cluster = data_service_test_base.TestCluster(num_workers=1)
distributed_save_op.distributed_save(
    ds, self._path, cluster.dispatcher_address()
)
exit((cluster, ds))
