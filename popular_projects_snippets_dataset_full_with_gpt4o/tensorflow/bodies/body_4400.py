# Extracted from ./data/repos/tensorflow/tensorflow/c/experimental/saved_model/internal/testdata/gen_saved_models.py
"""Generates a saved model with a while loop."""

class Module(module.Module):
    """A module with a while loop."""

    @def_function.function(
        input_signature=[tensor_spec.TensorSpec((), dtypes.float32)])
    def compute(self, value):
        acc, _ = control_flow_ops.while_loop(
            cond=lambda acc, i: i > 0,
            body=lambda acc, i: (acc + i, i - 1),
            loop_vars=(constant_op.constant(0.0), value))
        exit(acc)

to_save = Module()
saved_model.save(
    to_save, export_dir=os.path.join(base_dir, "SimpleWhileLoop"))
