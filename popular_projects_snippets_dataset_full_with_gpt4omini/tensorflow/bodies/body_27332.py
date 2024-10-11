# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
cluster = data_service_test_base.TestCluster(
    num_workers=2,
    data_transfer_protocol=self._get_data_transfer_protocol())

datasets = [
    dataset_ops.Dataset.range(20, output_type=dtypes.int32),
    dataset_ops.Dataset.from_tensor_slices(list(range(20, 40)))
]
dataset_ids = []

for ds in datasets:
    dataset_id = data_service_ops.register_dataset(
        cluster.dispatcher_address(), ds, compression=self._get_compression())
    dataset_ids.append(dataset_id)

# Read from both jobs in parallel, with 2 consumers for each job.
data_service_datasets = []
for _ in range(2):
    for dataset, dataset_id in zip(datasets, dataset_ids):
        ds = data_service_ops.from_dataset_id(
            "distributed_epoch",
            cluster.dispatcher.target,
            dataset_id,
            dataset.element_spec,
            data_transfer_protocol=self._get_data_transfer_protocol(),
            job_name="shared_job")
        data_service_datasets.append(ds)
ds = dataset_ops.Dataset.from_tensor_slices(data_service_datasets)
ds = ds.interleave(lambda x: x, cycle_length=len(data_service_datasets))

self.assertDatasetProduces(ds, list(range(40)), assert_items_equal=True)
