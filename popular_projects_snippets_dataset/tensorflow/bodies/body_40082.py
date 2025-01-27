# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
primal, tangent = _jvp(math_ops.sin, (constant_op.constant(0.1),),
                       (constant_op.constant(0.2),))
self.assertAllClose(math_ops.sin(0.1), primal)
self.assertAllClose(math_ops.cos(0.1) * 0.2, tangent)
