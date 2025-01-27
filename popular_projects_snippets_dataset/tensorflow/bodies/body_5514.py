# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/cross_device_ops_test.py
if use_strategy_object:
    with test_object.scope():
        exit(test_object.extended.batch_reduce_to(reduce_op,
                                                    value_destination_pairs,
                                                    hints))
else:
    exit(test_object.batch_reduce(reduce_op, value_destination_pairs,
                                    hints))
