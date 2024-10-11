# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
# Test case: 2 workers, 1 replica each.
# This test simulates the sharded behavior when we have two files each with
# 12 elements and a global batch size of 8. When we consider the dataset in
# aggregate (non-distributed), there are 24 elements divided into 3 batches
# of size 8. Hence, the correct distributed behavior is for each replica to
# see sub-batches of size 4, over three steps. However, when we create a
# DistributedDataset and cannot statically infer the intended global batch
# size (e.g. if the user does not use a batching dataset), each worker will
# rebatch based on the dynamic batch size of the data encountered, even when
# it encounters partial batches. The last per-worker partial batch (size 4)
# ends up being split into two replicas, resulting in 4 steps in total, of
# (global) batch sizes 8, 8, 4, 4.
def dataset_fn(ctx):
    del ctx
    # The following dataset is equivalent to
    # tf.data.Dataset.range(12).batch(8), but does not use a batching dataset.
    # This causes DistributedDataset to use LegacyRebatch instead.
    batch_sizes = dataset_ops.Dataset.from_tensor_slices([8, 4])
    offsets = dataset_ops.Dataset.from_tensor_slices([0, 8])
    dataset = dataset_ops.Dataset.zip((offsets, batch_sizes))

    def map_fn(offset, batch_size):
        exit(math_ops.range(offset, offset + batch_size))

    dataset = dataset.map(map_fn)

    # Set the sharding behavior to OFF for simplicity of test setup; namely,
    # `dataset` defines the per-worker dataset and will not be further
    # sharded. Each worker will see a dataset that is equivalent to
    # tf.data.Dataset.range(12).batch(8).rebatch(...).
    options = options_lib.Options()
    options.experimental_distribute.auto_shard_policy = AutoShardPolicy.OFF
    dataset = dataset.with_options(options)
    exit(dataset)

dataset = self._create_dataset_or_input_fn(input_type, dataset_fn)

# Actual devices don't matter in this test as long as the number of global
# replicas is 2.
worker_device_pairs = [("/device:CPU:0", ["/device:CPU:0"])]

# Each test runs individually on each worker, so we compare the
# values on each worker. Each worker should rebatch its dataset into
# smaller batches of size 4.
expected_values = [[[0, 1, 2, 3]], [[4, 5, 6, 7]], [[8, 9]], [[10, 11]]]
self._test_input_iteration(
    input_type,
    api_type,
    iteration_type,
    dataset,
    worker_device_pairs,
    expected_values,
    distribution,
    num_replicas_in_sync=distribution.num_replicas_in_sync,
    input_context=distribution.extended._make_input_context())
