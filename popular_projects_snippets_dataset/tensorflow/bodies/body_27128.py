# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/coordinated_read_test.py
cluster = data_service_test_base.TestCluster(num_workers=1)
ds = self.make_distributed_dataset(
    dataset_ops.Dataset.range(10).repeat(),
    cluster,
    job_name="test",
    consumer_index=0,
    num_consumers=2)
self.assertEqual(self.evaluate(ds.cardinality()), dataset_ops.INFINITE)
