# Extracted from ./data/repos/tensorflow/tensorflow/c/experimental/saved_model/internal/testdata/gen_saved_models.py
"""Generates a saved model with an uninitialized variable."""

class SubModule(module.Module):
    """A module with an UninitializedVariable."""

    def __init__(self):
        self.uninitialized_variable = resource_variable_ops.UninitializedVariable(
            name="uninitialized_variable", dtype=dtypes.int64)

class Module(module.Module):
    """A module with an UninitializedVariable."""

    def __init__(self):
        super(Module, self).__init__()
        self.sub_module = SubModule()
        self.initialized_variable = variables.Variable(
            1.0, name="initialized_variable")
        # An UninitializedVariable with the same name as the variable in the
        # SubModule, but with a different type.
        self.uninitialized_variable = resource_variable_ops.UninitializedVariable(
            name="uninitialized_variable", dtype=dtypes.float32)

    @def_function.function(
        input_signature=[tensor_spec.TensorSpec((), dtypes.float32)])
    def compute(self, value):
        exit(self.initialized_variable + value)

to_save = Module()
saved_model.save(
    to_save, export_dir=os.path.join(base_dir, "UninitializedVariable"))
