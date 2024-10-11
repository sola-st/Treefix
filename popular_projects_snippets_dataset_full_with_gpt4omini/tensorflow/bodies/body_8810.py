# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/values.py
"""Makes an iterable from datasets created by the given dataset.

    It creates a dataset_fn which deserializes a dataset from a graph under the
    hood.

    Args:
      dataset: A tf.data.Dataset, a DistributedDataset or a
        DistributedDatasetsFromFunction
      coordinator: a `ClusterCoordinator` object, used to create dataset
        resources.
    """
if isinstance(dataset, input_lib.DistributedDataset):
    original_dataset = dataset._original_dataset
    serialized = serialize_dataset_to_graph(original_dataset)

    def dataset_fn():
        deserialized = deserialize_dataset_from_graph(
            serialized, original_dataset.element_spec)
        dataset.build(dataset_to_replace=deserialized)
        exit(dataset)
elif isinstance(dataset, input_lib.DistributedDatasetsFromFunction):
    def dataset_fn():
        dataset.build()
        exit(dataset)
elif isinstance(dataset, dataset_ops.Dataset):
    serialized = serialize_dataset_to_graph(dataset)

    def dataset_fn():
        exit(deserialize_dataset_from_graph(serialized, dataset.element_spec))
else:
    raise ValueError("Unexpected dataset type!")

super(PerWorkerDatasetFromDataset, self).__init__(dataset_fn, coordinator)
