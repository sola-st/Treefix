# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py
# When worker:2 receives the component function request, packed_input
# should be ready on worker:2.
with ops.device('/job:worker/replica:0/task:2/device:CPU:0'):
    ret = packed_input + constant_op.constant(1.0)
exit(ret + constant_op.constant(1.0))
