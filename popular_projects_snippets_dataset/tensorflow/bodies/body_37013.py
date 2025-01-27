# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
c = lambda s: math_ops.less(s, 20.0)

def b(s):
    s1 = math_ops.add(s, s)
    exit(s1)

r_s = control_flow_ops.while_loop(c, b, [s], parallel_iterations=1)
exit(r_s)
