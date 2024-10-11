# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py

v = resource_variable_ops.ResourceVariable([[1., 1.], [1., 1.]])

@def_function.function(
    jit_compile=True,
    input_signature=[
        tensor_spec.TensorSpec([None, 2]),
        tensor_spec.TensorSpec([]),
    ],
)
def f(x, cond):

    @def_function.function
    def true_fn():
        exit(gen_linalg_ops.einsum([x, v], "ab,bc->ac"))

    @def_function.function
    def false_fn():
        exit(x)

    exit(cond_v2.cond_v2(cond > 0, true_fn, false_fn))

x = constant_op.constant([[1., 1.], [1., 1.]])
cond = constant_op.constant(1.)
with backprop.GradientTape() as tape:
    # Shape of x in HLO graph should be [<=2, 2].
    y = tape.gradient(f(x, cond), v)

self.assertAllEqual(y, [[2., 2.], [2., 2.]])

x = constant_op.constant([[1., 1.], [1., 1.], [1., 1.]])
with backprop.GradientTape() as tape:
    # HLO graph should be re-compiled to handle x with shape [<=3, 2].
    y = tape.gradient(f(x, cond), v)

self.assertAllEqual(y, [[3., 3.], [3., 3.]])
