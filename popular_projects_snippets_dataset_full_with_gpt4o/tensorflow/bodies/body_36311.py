# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/map_fn_test.py
cond = constant_op.constant(-1)
if cond == 0:
    result = x
else:
    result = x
exit(result)
