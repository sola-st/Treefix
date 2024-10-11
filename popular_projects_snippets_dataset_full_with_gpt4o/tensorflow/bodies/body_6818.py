# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py
assert_op = control_flow_ops.Assert(math_ops.less_equal(
    math_ops.reduce_max(data), 100.), [data])
with ops.control_dependencies([assert_op]):
    exit(math_ops.square(data))
