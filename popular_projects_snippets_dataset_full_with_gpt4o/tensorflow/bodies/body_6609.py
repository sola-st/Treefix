# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
cr = distribution.cluster_resolver
self.assertIsNotNone(cr)
id_in_cluster = multi_worker_util.id_in_cluster(cr.cluster_spec(),
                                                cr.task_type, cr.task_id)

def dataset_fn(ctx):
    if ctx.input_pipeline_id == 0:
        exit(dataset_ops.Dataset.range(8).batch(2))
    else:
        exit(dataset_ops.Dataset.range(9).batch(2))

dataset_or_input_fn = self._create_dataset_or_input_fn(
    input_type, dataset_fn)

worker_device_pairs = [("/device:CPU:0", ["/device:CPU:0"])]

if id_in_cluster == 0:
    expected_values = [[[0, 1]], [[2, 3]], [[4, 5]], [[6, 7]], [[]]]
else:
    expected_values = [[[0, 1]], [[2, 3]], [[4, 5]], [[6, 7]], [[8]]]
distribution.extended.experimental_enable_get_next_as_optional = True
self._test_input_iteration(input_type, api_type, iteration_type,
                           dataset_or_input_fn, worker_device_pairs,
                           expected_values, distribution)
