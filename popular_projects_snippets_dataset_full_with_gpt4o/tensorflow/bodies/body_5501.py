# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/cross_device_ops_test.py
if context.num_gpus() < sum(1 for d in devices if "GPU" in d.upper()):
    self.skipTest("Not enough GPUs")

with self.cached_session() as sess:
    values = [constant_op.constant(float(d)) for d in range(len(devices))]
    per_replica = _make_per_replica(values, devices)
    mean = (len(devices) - 1.) / 2.

    values_2 = [constant_op.constant(d + 1.0) for d in range(len(devices))]
    per_replica_2 = _make_per_replica(values_2, devices)
    mean_2 = mean + 1.

    destination_mirrored = _fake_mirrored(1., devices)
    destination_different = _fake_mirrored(1.,
                                           device_util.resolve(_cpu_device))
    destination_str = device_util.resolve(_cpu_device)

    all_destinations = [
        destination_mirrored,
        destination_different,
        destination_str,
    ]

    # test reduce()
    for destinations in all_destinations:
        self._assert_mirrored_equal(
            cross_device_ops.reduce(
                reduce_util.ReduceOp.MEAN,
                per_replica,
                destinations=destinations), _fake_mirrored(mean, destinations),
            sess)
        self._assert_mirrored_equal(
            cross_device_ops.reduce(
                reduce_util.ReduceOp.MEAN,
                per_replica_2,
                destinations=destinations),
            _fake_mirrored(mean_2, destinations), sess)
        self._assert_mirrored_equal(
            cross_device_ops.reduce(
                reduce_util.ReduceOp.SUM,
                per_replica,
                destinations=destinations),
            _fake_mirrored(mean * len(devices), destinations), sess)
        self._assert_mirrored_equal(
            cross_device_ops.reduce(
                reduce_util.ReduceOp.SUM,
                per_replica_2,
                destinations=destinations),
            _fake_mirrored(mean_2 * len(devices), destinations), sess)

    # test batch_reduce()
    for d1, d2 in itertools.product(all_destinations, all_destinations):
        self._assert_mirrored_equal(
            cross_device_ops.batch_reduce(reduce_util.ReduceOp.MEAN,
                                          [(per_replica, d1),
                                           (per_replica_2, d2)]),
            [_fake_mirrored(mean, d1),
             _fake_mirrored(mean_2, d2)], sess)
        self._assert_mirrored_equal(
            cross_device_ops.batch_reduce(reduce_util.ReduceOp.SUM,
                                          [(per_replica, d1),
                                           (per_replica_2, d2)]),
            [
                _fake_mirrored(mean * len(devices), d1),
                _fake_mirrored(mean_2 * len(devices), d2)
            ], sess)

    # test broadcast()
    for destinations in all_destinations:
        self._assert_mirrored_equal(
            cross_device_ops.broadcast(constant_op.constant(1.), destinations),
            _fake_mirrored(1., destinations), sess)
