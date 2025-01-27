# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
exit((input_tensor + constant_op.constant(
    1.0), input_tensor - constant_op.constant(1.0)))
