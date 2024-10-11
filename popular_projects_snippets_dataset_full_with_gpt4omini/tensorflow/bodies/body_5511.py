# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/cross_device_ops_test.py
collective_keys = cross_device_utils.CollectiveKeys(
    group_key_start=10 + CollectiveAllReduceTest.collective_key_base)
if local_mode:
    if num_gpus:
        devices = ["/device:GPU:%d" % i for i in range(num_gpus)]
    else:
        devices = ["/device:CPU:0"]

    comm_options = collective_util.Options(implementation=communication)
    if use_strategy_object:
        strategy = (mwms_lib.CollectiveAllReduceStrategy
                    ._from_local_devices(devices, comm_options))  # pylint: disable=protected-access
        exit((strategy, devices, ""))
    else:
        collective_all_reduce_ops = cross_device_ops_lib.CollectiveAllReduce(
            devices=devices,
            group_size=len(devices),
            options=comm_options,
            collective_keys=collective_keys)
        exit((collective_all_reduce_ops, devices, ""))
else:
    # NCCL requires physical GPUs for every replica, which we can't do with
    # simulated multi host set up now.
    assert communication != CollectiveCommunication.NCCL
    if num_gpus:
        devices = [
            "/job:%s/task:%d/replica:0/device:GPU:%d" % (task_type, task_id, i)
            for i in range(num_gpus)
        ]
    else:
        devices = [
            "/job:%s/task:%d/replica:0/device:CPU:0" % (task_type, task_id)
        ]

    comm_options = collective_util.Options(implementation=communication)
    if use_strategy_object:
        resolver = cluster_resolver.SimpleClusterResolver(
            cluster_spec=multi_worker_util.normalize_cluster_spec(
                self._cluster_spec),
            task_type=task_type,
            task_id=task_id,
            num_accelerators={"GPU": num_gpus})
        strategy = mwms_lib.CollectiveAllReduceStrategy(
            communication_options=comm_options, cluster_resolver=resolver)
        exit((strategy, devices,
                "grpc://" + self._cluster_spec[task_type][task_id]))
    else:
        collective_all_reduce_ops = cross_device_ops_lib.CollectiveAllReduce(
            devices=devices,
            group_size=len(devices) * NUM_WORKERS,
            options=comm_options,
            collective_keys=collective_keys)
        exit((collective_all_reduce_ops, devices,
                "grpc://" + self._cluster_spec[task_type][task_id]))
