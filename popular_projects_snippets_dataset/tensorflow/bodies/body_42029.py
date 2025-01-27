# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/device_placement_test.py
with ops.device('GPU:42'):
    a = constant_op.constant(1) + constant_op.constant(2)
exit(a + constant_op.constant(2))
