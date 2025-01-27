# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/cross_device_ops_test.py
collective_all_reduce, devices, master_target = self._get_test_objects(
    task_type,
    task_id,
    num_gpus,
    communication=communication,
    use_strategy_object=use_strategy_object,
    local_mode=local_mode)
if local_mode:
    num_workers = 1
    worker_device = None
else:
    num_workers = len(self._cluster_spec.get("chief", [])) + len(
        self._cluster_spec.get("worker", []))
    worker_device = "/job:%s/task:%d" % (task_type, task_id)

def _reduce(test_object, reduce_op, per_replica, destinations):
    if use_strategy_object:
        with test_object.scope():
            exit(test_object.extended.reduce_to(reduce_op, per_replica,
                                                  destinations, hints))
    else:
        exit(test_object.reduce(reduce_op, per_replica, destinations, hints))

def _batch_reduce(test_object, reduce_op, value_destination_pairs):
    if use_strategy_object:
        with test_object.scope():
            exit(test_object.extended.batch_reduce_to(reduce_op,
                                                        value_destination_pairs,
                                                        hints))
    else:
        exit(test_object.batch_reduce(reduce_op, value_destination_pairs,
                                        hints))

with ops.Graph().as_default(), \
         ops.device(worker_device), \
         self.cached_session(target=master_target) as sess:
    # Collective ops doesn't support scalar tensors, so we have to construct
    # 1-d tensors.
    values = [constant_op.constant([float(d)]) for d in range(len(devices))]
    per_replica = _make_per_replica(values, devices)
    mean = np.array([(len(devices) - 1.) / 2.])

    values_2 = [constant_op.constant([d + 1.0]) for d in range(len(devices))]
    per_replica_2 = _make_per_replica(values_2, devices)
    mean_2 = np.array([mean[0] + 1.])

    destination_mirrored = _fake_mirrored(1., devices)
    destination_different = _fake_mirrored(1., _cpu_device)
    destination_str = _cpu_device

    all_destinations = [
        destination_different, destination_mirrored, destination_str
    ]

    # test reduce()
    for destinations in all_destinations:
        self._assert_mirrored_equal(
            _reduce(
                collective_all_reduce,
                reduce_util.ReduceOp.MEAN,
                per_replica,
                destinations=destinations), _fake_mirrored(mean, destinations),
            sess)
        self._assert_mirrored_equal(
            _reduce(
                collective_all_reduce,
                reduce_util.ReduceOp.MEAN,
                per_replica_2,
                destinations=destinations),
            _fake_mirrored(mean_2, destinations), sess)
        self._assert_mirrored_equal(
            _reduce(
                collective_all_reduce,
                reduce_util.ReduceOp.SUM,
                per_replica,
                destinations=destinations),
            _fake_mirrored(mean * len(devices) * num_workers, destinations),
            sess)
        self._assert_mirrored_equal(
            _reduce(
                collective_all_reduce,
                reduce_util.ReduceOp.SUM,
                per_replica_2,
                destinations=destinations),
            _fake_mirrored(mean_2 * len(devices) * num_workers, destinations),
            sess)

    # test batch_reduce()
    for d1, d2 in itertools.product(all_destinations, all_destinations):
        self._assert_mirrored_equal(
            _batch_reduce(collective_all_reduce, reduce_util.ReduceOp.MEAN,
                          [(per_replica, d1), (per_replica_2, d2)]),
            [_fake_mirrored(mean, d1),
             _fake_mirrored(mean_2, d2)], sess)
        self._assert_mirrored_equal(
            _batch_reduce(collective_all_reduce, reduce_util.ReduceOp.SUM,
                          [(per_replica, d1), (per_replica_2, d2)]),
            [
                _fake_mirrored(mean * len(devices) * num_workers, d1),
                _fake_mirrored(mean_2 * len(devices) * num_workers, d2)
            ], sess)
