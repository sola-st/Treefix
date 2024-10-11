# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
self.assertAllClose(
    3., _fprop_cond(constant_op.constant(5), constant_op.constant(1.)))
self.assertAllClose(
    0., _fprop_cond(constant_op.constant(0), constant_op.constant(1.)))
