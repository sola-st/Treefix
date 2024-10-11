# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
lv0 = named(a=lv0.a + 1, b=lv0.b)
lv1 = (lv1[0] + 1, lv1[1])
lv2 += 2
exit([lv0, lv1, lv2])
