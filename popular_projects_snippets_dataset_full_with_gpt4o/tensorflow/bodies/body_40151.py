# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
x = constant_op.constant(2.0)
y = constant_op.constant(5.0)
tangents = (
    constant_op.constant([1., 0., 1.]),
    constant_op.constant([0., 1., 1.]),
)
with forwardprop.ForwardAccumulator._batch_accumulator((x, y),
                                                       tangents) as acc:
    z = x * y
self.assertAllClose(acc.jvp(z), constant_op.constant([5.0, 2.0, 7.0]))
