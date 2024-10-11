# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
cluster = data_service_test_base.TestCluster(
    num_workers=1, data_transfer_protocol="grpc")
range_ds = dataset_ops.Dataset.range(10)
dataset_id = data_service_ops.register_dataset(cluster.dispatcher.target,
                                               range_ds)
ds = data_service_ops.from_dataset_id(
    dataset_id=dataset_id,
    processing_mode="parallel_epochs",
    element_spec=range_ds.element_spec,
    service=cluster.dispatcher.target,
    data_transfer_protocol="grpc")
self.assertDatasetProduces(ds, list(range(10)))
