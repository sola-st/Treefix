# Extracted from ./data/repos/tensorflow/tensorflow/c/experimental/saved_model/internal/testdata/gen_saved_models.py
super(Module, self).__init__()
self.sub_module = SubModule()
self.initialized_variable = variables.Variable(
    1.0, name="initialized_variable")
# An UninitializedVariable with the same name as the variable in the
# SubModule, but with a different type.
self.uninitialized_variable = resource_variable_ops.UninitializedVariable(
    name="uninitialized_variable", dtype=dtypes.float32)
