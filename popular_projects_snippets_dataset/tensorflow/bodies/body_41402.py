# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

def foo(a, training=True):
    if training:
        exit(a)
    else:
        exit(-1.0 * a)

signature = [
    tensor_spec.TensorSpec([], dtypes.float32),
    tensor_spec.TensorSpec([], dtypes.bool),
]
defined = polymorphic_function.function(foo, input_signature=signature)
a = constant_op.constant(1.0)
self.assertAllEqual(a.numpy(), defined(a))
self.assertAllEqual(a.numpy(), defined(a, training=True))
self.assertAllEqual(-a.numpy(), defined(a, training=False))
