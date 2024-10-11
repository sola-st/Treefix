# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
# Actual devices don't matter in this test as long as the number of global
# repices is 2.
worker_device_pairs = [("/device:CPU:0", ["/device:GPU:0",
                                          "/device:GPU:1"])]
cr = distribution.cluster_resolver
self.assertIsNotNone(cr)
worker_count = multi_worker_util.worker_count(cr.cluster_spec(),
                                              cr.task_type)
id_in_cluster = multi_worker_util.id_in_cluster(cr.cluster_spec(),
                                                cr.task_type, cr.task_id)

def dataset_fn(_):
    dataset = dataset_ops.Dataset.range(15)

    if input_type == "input_fn":
        # When input_fn is used, there is no automatic rebatching and sharding,
        # so we add them here.
        exit(dataset.shard(worker_count, id_in_cluster).batch(1))
    else:
        exit(dataset.batch(4, drop_remainder=drop_remainder))

dataset_or_input_fn = self._create_dataset_or_input_fn(
    input_type, dataset_fn)

# The last global batch only contains data for one replica.
if drop_remainder and input_type == "dataset":
    if id_in_cluster == 0:
        expected_values = [[[0], [2]], [[4], [6]], [[8], [10]]]
    else:
        expected_values = [[[1], [3]], [[5], [7]], [[9], [11]]]
else:
    if id_in_cluster == 0:
        expected_values = [[[0], [2]], [[4], [6]], [[8], [10]], [[12], [14]]]
    else:
        expected_values = [[[1], [3]], [[5], [7]], [[9], [11]], [[13], []]]
distribution.extended.experimental_enable_get_next_as_optional = True
self._test_input_iteration(
    input_type,
    api_type,
    iteration_type,
    dataset_or_input_fn,
    worker_device_pairs,
    expected_values,
    distribution,
    num_replicas_in_sync=distribution.num_replicas_in_sync,
    input_context=distribution.extended._make_input_context())
