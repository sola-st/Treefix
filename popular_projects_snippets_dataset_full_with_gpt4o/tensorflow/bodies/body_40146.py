# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
self.assertAllClose(
    10., _fprop_while(constant_op.constant(5), constant_op.constant(1.)))
