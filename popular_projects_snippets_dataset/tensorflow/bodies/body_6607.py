# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
cr = distribution.cluster_resolver
self.assertIsNotNone(cr)
id_in_cluster = multi_worker_util.id_in_cluster(cr.cluster_spec(),
                                                cr.task_type, cr.task_id)
ds_option = options_lib.Options()
ds_option.experimental_distribute.auto_shard_policy = auto_shard_policy
dataset_fn = (
    lambda _: dataset_ops.Dataset.range(4).with_options(ds_option))
dataset_or_input_fn = self._create_dataset_or_input_fn(
    input_type, dataset_fn)

worker_device_pairs = [("/device:CPU:0", ["/device:CPU:0"])]
if auto_shard_policy == AutoShardPolicy.AUTO:
    if id_in_cluster == 0:
        expected_values = [[0], [2]]
    else:
        expected_values = [[1], [3]]
else:
    expected_values = [[0], [1], [2], [3]]
self._test_input_iteration(
    input_type,
    api_type,
    iteration_type,
    dataset_or_input_fn,
    worker_device_pairs,
    expected_values,
    distribution,
    input_context=distribution.extended._make_input_context())
