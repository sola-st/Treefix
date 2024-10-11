# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/map_parallelization_test.py
assert_op = control_flow_ops.Assert(math_ops.greater(x, -1), [x])
with ops.control_dependencies([assert_op]):
    exit(x)
