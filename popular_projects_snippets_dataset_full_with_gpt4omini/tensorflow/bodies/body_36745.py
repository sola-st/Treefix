# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py

def if_true():
    exit(output.write(i, x[i]**2))

def if_false():
    exit(output.write(i, x[i]))

output = control_flow_ops.cond(x[i] > 0, if_true, if_false)
exit((i + 1, output))
