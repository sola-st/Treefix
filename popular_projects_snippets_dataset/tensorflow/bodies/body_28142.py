# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_cluster_test.py
worker_config = config_pb2.ConfigProto()
worker_config.device_count["CPU"] = 2
worker, _ = test_util.create_local_cluster(
    1, 1, worker_config=worker_config)

with ops.device("/job:worker/replica:0/task:0/cpu:1"):
    dataset_3 = dataset_ops.Dataset.from_tensor_slices([1, 2, 3])
    iterator_3 = dataset_ops.make_one_shot_iterator(dataset_3)
    iterator_3_handle = iterator_3.string_handle()

with ops.device("/job:worker/replica:0/task:0/cpu:0"):
    remote_it = iterator_ops.Iterator.from_string_handle(
        iterator_3_handle, dataset_ops.get_legacy_output_types(dataset_3),
        dataset_ops.get_legacy_output_shapes(dataset_3))
    get_next_op = remote_it.get_next()

with session.Session(worker[0].target) as sess:
    with self.assertRaises(errors.InvalidArgumentError):
        sess.run(get_next_op)
