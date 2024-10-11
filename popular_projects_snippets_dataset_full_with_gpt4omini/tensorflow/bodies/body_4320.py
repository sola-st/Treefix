# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/input_util.py
datasets: List[Tuple[int, dataset_ops.DatasetV2]] = []

# Start with the batched the dataset.
local_dataset = self._batched_dataset

if self._batch_dim is not None:
    if self._num_clients_per_replica > 1:
        # If a replica is split over multiple clients then each batch needs to
        # be repeated before distribution as many times as there are clients
        # corresponding to that replica.
        local_dataset = self._repeat_batch(local_dataset,
                                           self._num_clients_per_replica)
        sharding_policy = data_service_ops.ShardingPolicy.DATA
    else:
        # Replicas are unique to each client, so FILE based sharding can be used
        # which is more performant since each worker does not need to read the
        # entire dataset.
        sharding_policy = data_service_ops.ShardingPolicy.FILE
else:
    # No batch dimension sharding specified so disable dataset sharding during
    # the distribute step.
    sharding_policy = data_service_ops.ShardingPolicy.OFF

# Apply distribution here (if specified) so all remaining transformations
# are executed locally.
if self._tf_data_service_config is not None:
    local_dataset = local_dataset.apply(
        data_service_ops.distribute(
            processing_mode=sharding_policy,
            service=self._tf_data_service_config.dispatcher_address,
            job_name=f'{self._tf_data_service_config.job_name}_{config.client_id()}',
            target_workers='LOCAL'))

for local_replica_idx, replica_id in enumerate(self._local_replica_ids):
    # Select the shard for the corresponding replica.
    dataset = local_dataset.shard(self._num_local_replicas, local_replica_idx)

    # Repeat each batch for each local device in the replica.
    dataset = self._repeat_batch(dataset, self._num_local_devices_per_replica)

    # Slice each shard further for all non-batch dim shards. If there is no
    # non-batch dim sharding, this slice is essentially a no-op.
    dataset = self._partition(dataset)

    # Apply prefetch as the last step. Since each batch is repeated, the
    # number of elements to prefetch has to be scaled by the same size.
    if self._prefetch is not None:
        dataset = dataset.prefetch(
            self._prefetch * self._num_local_devices_per_replica)

    datasets.append((replica_id, dataset))

exit(_DTensorIterator(datasets, self._element_spec, self._layouts,
                        self._num_local_devices_per_replica))
