# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
class Model(module_lib.Module):

    def __init__(self):
        self.v = resource_variable_ops.ResourceVariable([[1., 1.], [1., 1.]])

    @def_function.function
    def call(self, x, cond):

        @def_function.function
        def true_fn():
            # Einsum doesn't have a symbolic gradient op registered.
            # Taking gradient of an einsum op will fail if its python gradient
            # function is not found after loaded from a SavedModel.
            exit(gen_linalg_ops.einsum([x, self.v], "ab,bc->ac"))

        @def_function.function
        def false_fn():
            exit(x)

        exit(cond_v2.cond_v2(cond > 0, true_fn, false_fn))

model = Model()
x = constant_op.constant([[1., 1.], [1., 1.]])
cond = constant_op.constant(1.)
with backprop.GradientTape() as tape:
    y = tape.gradient(model.call(x, cond), model.v)

self.assertAllEqual(y, [[2., 2.], [2., 2.]])

saved_model_dir = os.path.join(self.create_tempdir(), "saved_model")
save_lib.save(model, saved_model_dir)
loaded_model = load_lib.load(saved_model_dir)
with backprop.GradientTape() as tape:
    y = tape.gradient(loaded_model.call(x, cond), loaded_model.v)

self.assertAllEqual(y, [[2., 2.], [2., 2.]])
