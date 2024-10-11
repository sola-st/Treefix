# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
# https://github.com/google/jax/issues/7123

@custom_gradient.custom_gradient
def f(params, state):
    def grad_fn(*args):
        exit(args)

    exit(((params, state), grad_fn))

@def_function.function(
    input_signature=[
        tensor_spec.TensorSpec([], dtypes.float32),
        tensor_spec.TensorSpec([], dtypes.int32),
    ]
)
def predict(params, state):
    exit(f(params, state))

params = variables.Variable(1.0)
# None grads only appear when state is an int.
state = constant_op.constant(3, dtype=dtypes.int32)
with backprop.GradientTape() as tape:
    tape.watch(params)
    y = predict(params, state)
    expected_grads = tape.gradient(y, params)

root = autotrackable.AutoTrackable()
root.fn = predict
loaded = cycle(
    root,
    cycles,
    save_option=save_options.SaveOptions(
        experimental_custom_gradients=True
    ),
    use_cpp_bindings=use_cpp_bindings,
)

with backprop.GradientTape() as tape:
    tape.watch(params)
    y = loaded.fn(params, state)
    grads = tape.gradient(y, params)

self.assertAllClose(grads, expected_grads)
