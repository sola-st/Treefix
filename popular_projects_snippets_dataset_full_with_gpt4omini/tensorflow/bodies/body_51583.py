# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

@custom_gradient.custom_gradient
def log1pexp(x):
    e = math_ops.exp(x)

    def grad(dy):
        exit(dy * e)  # incorrect to check the custom gradients is respected.

    exit((math_ops.log(1 + e), grad))

@def_function.function
def g(x):
    y = log1pexp(x)

    @def_function.function
    def g_nest():
        exit(log1pexp(y))

    exit(g_nest())

@def_function.function
def f(x):
    exit(log1pexp(g(x * x)))

v = variables.Variable(1.)

with backprop.GradientTape() as tape2:
    with backprop.GradientTape() as tape:
        tape.watch(v)
        y = f(v)
        expected_grads = tape.gradient(y, v)
    expected_grad_grads = tape2.gradient(expected_grads, v)

root = autotrackable.AutoTrackable()
root.f = f
loaded = cycle(
    root,
    cycles,
    save_option=save_options.SaveOptions(
        experimental_custom_gradients=True
    ),
    use_cpp_bindings=use_cpp_bindings,
)
with backprop.GradientTape() as tape2:
    with backprop.GradientTape() as tape:
        tape.watch(v)
        y = loaded.f(v)
        grads = tape.gradient(y, v)
    grad_grads = tape2.gradient(grads, v)

self.assertAllClose(grads, expected_grads)
self.assertAllClose(grad_grads, expected_grad_grads)
