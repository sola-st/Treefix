# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli_test.py
function = def_function.function(
    self.multiply,
    input_signature=[
        tensor_spec.TensorSpec(shape=(), dtype=dtypes.float32),
        tensor_spec.TensorSpec(shape=(), dtype=dtypes.float32)
    ])
self.pure_concrete_function = function.get_concrete_function()
super(DummyModel, self).__init__()
