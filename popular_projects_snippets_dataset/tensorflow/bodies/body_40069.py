# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
add_outputs = (constant_op.constant(4.),)
vp, = forwardprop._jvp_dispatch(
    op_name="Add",
    attr_tuple=(),
    inputs=(constant_op.constant(1.), constant_op.constant(3.)),
    outputs=add_outputs,
    tangents=(
        constant_op.constant(1.),
        constant_op.constant(5.),
    ))
self.assertAllClose(1. + 5., self.evaluate(vp))

mul_outputs = (constant_op.constant([20.]),)
vp, = forwardprop._jvp_dispatch(
    op_name="Mul",
    attr_tuple=(),
    inputs=(constant_op.constant([4.]), constant_op.constant([5.])),
    outputs=mul_outputs,
    tangents=(
        constant_op.constant([2.]),
        constant_op.constant([3.]),
    ))
self.assertAllClose([2. * 5. + 3. * 4.], self.evaluate(vp))
