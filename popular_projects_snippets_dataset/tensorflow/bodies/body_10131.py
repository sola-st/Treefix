# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
a = variables.Variable(2.)
b = variables.Variable(4.)
input_vars = [a, b]
self.evaluate(variables.global_variables_initializer())
if context.executing_eagerly():
    # TDOO(rmlarsen): Is there a more compact way of
    # writing this for multiple expressions?
    with backprop.GradientTape() as tape:
        tape.watch(input_vars)
        c_grad0 = tape.gradient(math_ops.divide(a, b), input_vars)
    with backprop.GradientTape() as tape:
        tape.watch(input_vars)
        c_grad1 = tape.gradient(math_ops.div(a, b), input_vars)
    with backprop.GradientTape() as tape:
        tape.watch(input_vars)
        c_grad2 = tape.gradient(math_ops.floordiv(a, b), input_vars)
else:
    c_grad0 = gradients.gradients(math_ops.divide(a, b), input_vars)
    c_grad1 = gradients.gradients(math_ops.div(a, b), input_vars)
    c_grad2 = gradients.gradients(math_ops.floordiv(a, b), input_vars)
self.assertAllEqual([self.evaluate(x) for x in c_grad0], [.25, -.125])
self.assertAllEqual([self.evaluate(x) for x in c_grad1], [.25, -.125])
self.assertAllEqual(
    [None if x is None else self.evaluate(x) for x in c_grad2],
    [None, None])
