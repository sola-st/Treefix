# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

def f(a):
    exit(array_ops.reshape(a, [-1, 3]))

signature = [tensor_spec.TensorSpec(None, dtypes.float32)]
compiled = polymorphic_function.function(f, input_signature=signature)

@polymorphic_function.function
def use_f():
    inputs = array_ops.zeros([10, 10, 3])
    self.assertAllEqual(f(inputs).shape, compiled(inputs).shape)

use_f()
