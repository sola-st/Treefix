# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
exit(_cond(pred, lambda: x - y, lambda: y * y, name=None))
