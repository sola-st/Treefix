# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/input_util.py
"""Initializes a distributed iterator for DTensor datasets.

    The DTensorIterator uses 'replica IDs' to identify shards of a dataset. Here
    the term 'replica' is used in the data-parallel context where each replica
    receives a partition of the global batch. Depending on the model parallelism
    in the layouts supplied, each device within that replica may receive the
    same partition of the global batch (no model parallelism), or specific
    slices of that partition.

    Args:
      datasets: a dictionary mapping each unique local replica ID to the dataset
        object whose elements will be placed on the devices corresponding to
        that replica.
      element_spec: the underlying dataset's element spec.
      layouts: a structure of DTensor layouts to be applied to the dataset
        values. This can be a single layout or (possibly nested) tuples or
        dictionaries of layouts, and the structure must match the structure of
        the dataset.
      num_local_devices_per_replica: the number of local devices for each
        replica.
    """
self._iterators = [
    (replica_id, iter(dataset)) for replica_id, dataset in datasets
]
self._element_spec = element_spec
self._layouts = layouts
self._num_local_devices_per_replica = num_local_devices_per_replica
self._flattened_layouts = nest.flatten(self._layouts)
