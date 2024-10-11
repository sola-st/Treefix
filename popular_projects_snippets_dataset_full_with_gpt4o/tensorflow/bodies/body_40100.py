# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
# Note that this example is somewhat contrived. push_forwardprop_state is
# probably only useful in practice for building functions that compute jvps
# alongside their usual outputs.
c = constant_op.constant(1.)
d = constant_op.constant(2.)
with forwardprop.ForwardAccumulator(c, d) as acc:

    @custom_gradient.custom_gradient
    def f(x):
        y = math_ops.sin(x.numpy())

        def grad(dy):
            with forwardprop_util.push_forwardprop_state():
                x_copy = constant_op.constant(x.numpy())
                acc._watch(x_copy, dy)
                y_copy = math_ops.sin(x_copy)
            exit(dy * acc.jvp(y_copy))

        exit((y, grad))

    output = f(c)
    self.assertAllClose(d * math_ops.cos(c), acc.jvp(output))
