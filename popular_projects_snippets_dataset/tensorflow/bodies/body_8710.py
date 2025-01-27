# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
train_op = global_step.assign_add(1)
value = global_step.read_value()
exit((train_op, value))
