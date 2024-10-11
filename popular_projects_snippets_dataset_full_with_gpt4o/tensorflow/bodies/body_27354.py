# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
cluster = data_service_test_base.TestCluster(
    num_workers=1, data_transfer_protocol="grpc")
ds = dataset_ops.Dataset.range(10)
ds = ds.apply(
    data_service_ops.distribute(
        processing_mode="parallel_epochs",
        service="grpc://" + cluster.dispatcher_address()))
self.assertDatasetProduces(ds, list(range(10)))
