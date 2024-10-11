# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/matrix_band_part_op_test.py
test_name = "_".join(["test", op_name, testcase_name])
if hasattr(test, test_name):
    raise RuntimeError("Test %s defined more than once" % test_name)
setattr(test, test_name, fn)
