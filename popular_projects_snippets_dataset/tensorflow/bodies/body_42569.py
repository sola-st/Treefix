# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context_test.py
with ops.device('CPU:0'):
    exit(x + constant_op.constant(1.))
