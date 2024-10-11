# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
add_outputs = (constant_op.constant(4.),)
jvp_flat = forwardprop._jvp_dispatch(
    op_name="Add",
    attr_tuple=(),
    inputs=(constant_op.constant(1.), constant_op.constant(3.)),
    outputs=add_outputs,
    tangents=(
        constant_op.constant([1., 2., 3.]),
        constant_op.constant([4., 5., 6.]),
    ),
    use_batch=True)

# Using evaluate and asserting with just a list works too
# but the output is more explicit this way
self.assertAllClose([constant_op.constant([1. + 4., 2. + 5., 3. + 6.])],
                    jvp_flat)

mul_outputs = (constant_op.constant([20.]),)
jvp_flat = forwardprop._jvp_dispatch(
    op_name="Mul",
    attr_tuple=(),
    inputs=(constant_op.constant([4.]), constant_op.constant([5.])),
    outputs=mul_outputs,
    tangents=(
        constant_op.constant([[1.], [0.], [1.]]),
        constant_op.constant([[0.], [1.], [1.]]),
    ),
    use_batch=True)
self.assertAllClose([constant_op.constant([[5.], [4.], [5. + 4.]])],
                    jvp_flat)
