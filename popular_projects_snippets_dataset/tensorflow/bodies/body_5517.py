# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/cross_device_ops_test.py
collective_all_reduce, devices, master_target = self._get_test_objects(
    task_type,
    task_id,
    num_gpus,
    communication=communication,
    local_mode=local_mode)
if local_mode:
    num_workers = 1
    worker_device = None
else:
    num_workers = len(self._cluster_spec.get("chief", [])) + len(
        self._cluster_spec.get("worker", []))
    worker_device = "/job:%s/task:%d" % (task_type, task_id)
    config = config_pb2.ConfigProto()
    # Disable coordination service for all tasks except task 0 to avoid
    # parallel init of the service singleton.
    if task_id != 0:
        config.experimental.coordination_config.service_type = ""
with ops.Graph().as_default(), \
         ops.device(worker_device), \
         self.cached_session(target=master_target, config=config) as sess:
    per_replica = self._get_indexed_slices(devices,
                                           (task_id or 0) * max(num_gpus, 1),
                                           variable_length)

    if batch_reduce:
        result = collective_all_reduce.batch_reduce(
            reduce_util.ReduceOp.SUM, [(per_replica, per_replica)])[0]
    else:
        result = collective_all_reduce.reduce(reduce_util.ReduceOp.SUM,
                                              per_replica, per_replica)
    if num_gpus > 1:
        self.assertIsInstance(result, value_lib.Mirrored)

    run_options = config_pb2.RunOptions()
    run_options.experimental.collective_graph_key = 7
    if num_gpus > 1:
        result = sess.run([ops.convert_to_tensor(v) for v in result.values],
                          options=run_options)[0]
    else:
        result = sess.run(ops.convert_to_tensor(result), options=run_options)

    # Reduce the same indexed slices on CPU locally as our expected results.
    devices_cpu = [(worker_device or "") + "/device:CPU:0"] * (
        max(num_gpus, 1) * num_workers)
    per_replica_on_cpu = self._get_indexed_slices(
        devices_cpu, 0, variable_length, as_per_replica=False)
    expected_result = cross_device_utils.aggregate_tensors_or_indexed_slices(
        per_replica_on_cpu)
    expected_result = sess.run(ops.convert_to_tensor(expected_result))

    self.assertAllEqual(expected_result, result)
