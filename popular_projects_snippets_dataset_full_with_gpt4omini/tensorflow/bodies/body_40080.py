# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
x = constant_op.constant(-2.)
with forwardprop.ForwardAccumulator(x, 1.5) as acc:
    self.assertAllClose(1.5, acc.jvp(x))
    y = 4. * x
    self.assertAllClose(6., acc.jvp(y))
    with self.assertRaisesRegex(ValueError, "already recording"):
        with acc:
            pass
z = 4. * x
self.assertIsNone(acc.jvp(z))
with acc:
    yy = y * y
self.assertAllClose(6. * -8. * 2., acc.jvp(yy))
