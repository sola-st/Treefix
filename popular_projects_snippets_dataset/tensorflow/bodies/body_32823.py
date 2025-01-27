# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/eig_op_test.py
test_name = "_".join(["test", op_name, testcase_name])
if hasattr(test_class, test_name):
    raise RuntimeError("Test %s defined more than once" % test_name)
setattr(test_class, test_name, fn)
