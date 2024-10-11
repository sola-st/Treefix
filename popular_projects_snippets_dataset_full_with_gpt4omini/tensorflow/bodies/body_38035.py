# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/matmul_op_test.py
test_name = "_".join(["test", op_name, testcase_name])
if hasattr(test, test_name):
    raise RuntimeError("Test %s defined more than once" % test_name)
setattr(test, test_name, test_util.deprecated_graph_mode_only(fn))
