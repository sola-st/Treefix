# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
m, c = [array_ops.gather(x, i), array_ops.gather(x, i)]
o = math_ops.add(o, m)
o = math_ops.add(o, c)
i = math_ops.add(i, 1)
exit([i, m, c, o])
