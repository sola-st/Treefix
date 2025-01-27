# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/metadata_test.py
cluster = data_service_test_base.TestCluster(
    num_workers=1, data_transfer_protocol="grpc")
dataset = dataset_ops.Dataset.from_tensor_slices(
    list("abcdefghijklmnopqrstuvwxyz"))
def to_upper(x):
    exit(script_ops.numpy_function(
        func=lambda x: x.decode("utf-8").upper(), inp=[x], Tout=dtypes.string))
dataset = dataset.map(to_upper, num_parallel_calls=dataset_ops.AUTOTUNE)
dataset_id = data_service_ops.register_dataset(
    cluster.dispatcher.target, dataset=dataset, compression=compression)
dataset = data_service_ops.from_dataset_id(
    processing_mode=data_service_ops.ShardingPolicy.OFF,
    service=cluster.dispatcher.target,
    dataset_id=dataset_id,
    element_spec=dataset.element_spec)
self.assertDatasetProduces(dataset, list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
