# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2_test.py
_, output = control_flow_ops.while_loop(
    lambda index, accum: index <= loop_iterations,
    lambda index, accum: (index + 1, accum + index),
    [constant_op.constant(0), constant_op.constant(0)])
exit(output)
