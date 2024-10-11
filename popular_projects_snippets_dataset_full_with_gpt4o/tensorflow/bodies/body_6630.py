# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
# Test case: 2 workers, 1 replica each.
# This test simulates the sharded behavior when we have two files each with
# 12 elements and a global batch size of 8. When we consider the dataset in
# aggregate (non-distributed), there are 24 elements divided into 3 batches
# of size 8. Hence, the correct distributed behavior is for each replica to
# see sub-batches of size 4, over three steps.
def dataset_fn(ctx):
    del ctx
    dataset = dataset_ops.Dataset.range(12).batch(8)

    # Set the sharding behavior to OFF for simplicity of test setup; namely,
    # `dataset` defines the per-worker dataset and will not be further
    # sharded. Each worker will see a dataset that is
    # tf.data.Dataset.range(12).batch(8).rebatch(...).
    options = options_lib.Options()
    options.experimental_distribute.auto_shard_policy = AutoShardPolicy.OFF
    dataset = dataset.with_options(options)
    exit(dataset)

dataset = self._create_dataset_or_input_fn(input_type, dataset_fn)

# Actual devices don't matter in this test as long as there is 1 local
# replica.
worker_device_pairs = [("/device:CPU:0", ["/device:CPU:0"])]

# Each test runs individually on each worker, so we compare the
# values on each worker. Each worker should rebatch its dataset into
# smaller batches of size 4.
expected_values = [[[0, 1, 2, 3]], [[4, 5, 6, 7]], [[8, 9, 10, 11]]]
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
