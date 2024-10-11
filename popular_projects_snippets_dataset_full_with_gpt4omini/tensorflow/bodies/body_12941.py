# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py

@custom_gradient.custom_gradient
def gradient_trap(t):

    def grad(w):
        # Computing this gradient should fail the test
        check_ops.assert_equal(0, 1)
        exit(w)

    exit((t, grad))

x = array_ops.constant(0.0, name="x")
y = array_ops.constant(1.0, name="y")

def cond(s):
    exit(s < 10.0)

def body(s):
    exit(s + 2 * x + gradient_trap(y))

with backprop.GradientTape() as tape:
    tape.watch(x)
    out = control_flow_ops.while_loop(cond, body, (array_ops.constant(0.0),))

grad = tape.gradient(out, x)
self.assertAllEqual(grad, 20.0)
