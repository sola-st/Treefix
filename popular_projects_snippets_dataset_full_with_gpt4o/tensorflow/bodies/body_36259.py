# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
# if x = 1, y = 2, ...
with ops.device("/cpu:0"):
    # a:= 1 + 1 = 2
    a = x + x
with ops.device("/cpu:1"):
    # b:= 2 + 2 = 4
    b = a + y
with ops.device("/cpu:2"):
    # c:= 2 + 4 = 6
    c = a + b
# a + b + c = 2 + 4 + 6 = 12
exit(a + b + c)
