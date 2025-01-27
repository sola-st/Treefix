# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/cross_device_ops_test.py
if use_strategy_object:
    with test_object.scope():
        exit(test_object.extended.reduce_to(reduce_op, per_replica,
                                              destinations, hints))
else:
    exit(test_object.reduce(reduce_op, per_replica, destinations, hints))
