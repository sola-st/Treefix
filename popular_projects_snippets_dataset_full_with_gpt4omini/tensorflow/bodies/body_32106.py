# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/as_string_op_test.py
exit([s.decode("ascii").replace("-nan", "nan") for s in s_l])
