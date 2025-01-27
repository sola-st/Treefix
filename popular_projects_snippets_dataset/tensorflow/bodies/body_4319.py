# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/input_util.py
"""Creates a DTensorDataset.

    DTensorDataset automatically handles distribution of the dataset elements to
    each client's devices. It can be used to create an iterator that returns
    DTensors of the input data on each iteration.

    DTensorDataset works best with unbatched datasets. It takes the mesh and the
    provided layouts to automatically calculate how to batch the input locally
    for each replica.

    If the provided dataset is already batched according to the per-replica
    batch size, then `dataset_already_batched` must be set and DTensorDataset
    will check that the batch size is consistent with the intended
    `global_batch_size` using the layout information. Each replica receives a
    separate slice of the global batch, thus the per-replica batch size can be
    computed as the global batch size divided by the number of model replicas.
    For a DTensor mesh, the number of replicas is equal to the size of the
    mesh's batch dimension.

    TODO(b/223275517): add support for input datasets that are already batched
    to the global batch size.

    Args:
      dataset: a `tf.data.Dataset` object.
      mesh: the DTensor mesh to place the dataset batches on.
      layouts: a structure of DTensor layouts to be applied to the input dataset
        values. This can be a single layout or (possibly nested) tuples or
        dictionaries of layouts, and the structure must match the structure of
        the dataset. Either all or none of the layouts should be sharded on the
        batch dimension; having only a subset of layouts batch sharded will not
        work and raises a ValueError.
      global_batch_size: the desired global batch size.
      dataset_already_batched: must be set only if the dataset is already
        batched to the per-replica batch size. The batched dataset must have
        `drop_remainder=True` set since DTensor requires static shapes for
        slicing the input tensors.
      batch_dim: the mesh dimension on which the input's batch dimension is
        sharded. Set to None if the input layouts do not shard on the batch
        dimension.
      prefetch: number of batches to prefetch using Dataset.prefetch.
      tf_data_service_config: if operating in multi-client mode, this config
        specifies the tf.data service configuration to use.

    Raises:
      ValueError: on any of the following situations,
        1. if the structures and ranks of layouts and the dataset do not match.
        2. if the shapes in the dataset's spec are not fully defined.
        3. if batch_dim is specified and all layouts are not batch-sharded.
        4. if per_replica_batch_size is specified for an already batched Dataset
           but it does not match the expected per-replica size based on the
           provided mesh.
      TypeError: if type of structures of layouts and the dataset do not match.
    """
super().__init__(dataset, dataset_ops.to_variant(dataset))

self._mesh = mesh
self._layouts = layouts
self._batch_dim = batch_dim
self._prefetch = prefetch
self._tf_data_service_config = tf_data_service_config

self._element_spec = dataset.element_spec

nest.assert_same_structure(self._element_spec, self._layouts)
flattened_layouts = nest.flatten(self._layouts)
flattened_elem_spec = nest.flatten(self._element_spec)

if batch_dim:
    num_global_replicas = mesh.dim_size(batch_dim)
    self._local_replica_ids = list(
        dict.fromkeys(
            [loc[batch_dim] for loc in mesh.local_device_locations()]))

    for layout in flattened_layouts:
        if batch_dim != layout.sharding_specs[0]:
            raise ValueError(
                ('batch_dim %s was specified but at least one layout did not '
                 'contain it: %s') % (batch_dim, layout))
else:
    # Only one replica since there is no sharding on the batch dimension.
    num_global_replicas = 1
    self._local_replica_ids = [0]

# Validate layout and element spec compatibility, and raise ValueError if
# invalid.
_validate_input(
    flattened_layouts,
    flattened_elem_spec,
    dataset_already_batched=dataset_already_batched)

expected_batch_size = global_batch_size // num_global_replicas
if not dataset_already_batched:
    self._batched_dataset = dataset.batch(
        expected_batch_size, drop_remainder=True)
else:
    per_replica_batch_size = flattened_elem_spec[0].shape.as_list()[0]
    if per_replica_batch_size != expected_batch_size:
        raise ValueError(
            ('per_replica_batch_size does not matched expected size based on '
             'the mesh, got %d but expected %d.') %
            (per_replica_batch_size, expected_batch_size))
    self._batched_dataset = dataset

num_global_devices_per_replica = config.num_global_devices(
    mesh.device_type()) // num_global_replicas
self._num_local_replicas = len(self._local_replica_ids)
self._num_local_devices_per_replica = mesh.num_local_devices(
) // self._num_local_replicas
# The number of clients each replica is split over.
self._num_clients_per_replica = (
    num_global_devices_per_replica //
    self._num_local_devices_per_replica)
# In the case where a replica is split across multiple clients, an offset
# needs to be added to the index used by the partitioning logic such that
# the local devices on that client can be correctly matched to slices of the
# input tensor(s). If replicas are wholly contained within a client, then
# this offset is always 0.
self._partition_offset = (config.client_id() % self._num_clients_per_replica
                         ) * self._num_local_devices_per_replica

# Helper data structures used in partitioning the dataset tensors.
self._all_shard_counts = [
    _shard_counts(layout, batch_dim) for layout in flattened_layouts
]
self._index_matrices = [
    _index_matrix(layout, elem_spec) for layout, elem_spec in zip(
        flattened_layouts, flattened_elem_spec)
]
