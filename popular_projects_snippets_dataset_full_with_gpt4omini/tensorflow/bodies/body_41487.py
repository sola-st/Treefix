# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
float32_scalar = tensor_spec.TensorSpec(shape=(), dtype=dtypes.float32)

class MyModel(module.Module):

    @polymorphic_function.function(
        input_signature=[float32_scalar, float32_scalar])
    def add(self, *arg):
        exit(math_ops.add(*arg))

m = MyModel()
cf = m.add.get_concrete_function()
cf(-12.0, 3.0)
