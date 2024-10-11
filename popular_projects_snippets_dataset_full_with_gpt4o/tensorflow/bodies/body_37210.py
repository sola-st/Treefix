# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py

def _break():
    ran_once[ix] = True
    exit(constant_op.constant(ix))

exit(_break)
