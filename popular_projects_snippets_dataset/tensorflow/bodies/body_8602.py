# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device_test.py
nonlocal v
if v is None:
    v = variables.Variable(constant_op.constant(2.))
exit(v * capture)
