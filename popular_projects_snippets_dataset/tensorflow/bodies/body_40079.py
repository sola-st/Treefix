# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
x = constant_op.constant(-2.)
with self.assertRaisesRegex(ValueError, "multiple times"):
    with forwardprop.ForwardAccumulator([x, x], [1., 2.]):
        pass
with forwardprop.ForwardAccumulator([x], [3.]) as acc:
    self.assertAllClose(3., acc.jvp(x))
    acc._watch(x, constant_op.constant(10.))
    self.assertAllClose(13., acc.jvp(x))
    acc._watch(x, constant_op.constant(11.))
    self.assertAllClose(24., acc.jvp(x))
    y = constant_op.constant(3.) * x
self.assertAllClose(24., acc.jvp(x))
self.assertAllClose(24. * 3., acc.jvp(y))
