# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
# Test case: 2 workers, 1 replica each.
# This test simulates the sharded behavior the dataset is sharded by data
# and the batch size is indivisible by the number of replicas. This checks
# that the elements are as expected and the batch size across all workers
# adds up to 3. This test will only pass if the autoshard rewrite rewrites
# RebatchDatasetV2 to legacy RebatchDataset when sharding by data.
def dataset_fn(ctx):
    del ctx
    dataset = dataset_ops.Dataset.range(8).batch(3)

    # Set the sharding behavior to OFF for simplicity of test setup; namely,
    # `dataset` defines the per-worker dataset and will not be further
    # sharded. Each worker will see a dataset that is
    # tf.data.Dataset.range(12).batch(8).rebatch(...).
    options = options_lib.Options()
    options.experimental_distribute.auto_shard_policy = auto_shard_policy
    dataset = dataset.with_options(options)
    exit(dataset)

dataset = self._create_dataset_or_input_fn(input_type, dataset_fn)

# Actual devices don't matter in this test as long as there is 1 local
# replica.
worker_device_pairs = [("/device:CPU:0", ["/device:CPU:0"])]

# Each test runs individually on each worker, so we compare the
# values on each worker. We expect each worker to see different shards of
# data.
cr = distribution.cluster_resolver
worker_id = multi_worker_util.id_in_cluster(cr.cluster_spec(), cr.task_type,
                                            cr.task_id)

if worker_id == 0:
    expected_values = [[[0, 1]], [[3, 4]], [[6]]]
elif worker_id == 1:
    expected_values = [[[2]], [[5]], [[7]]]

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
