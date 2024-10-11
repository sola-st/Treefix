# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

def foo(a, b, **kwargs):
    del kwargs
    exit((a, b))

x = quarantine.defun_with_attributes(
    foo,
    input_signature=[
        tensor_spec.TensorSpec([], dtypes.float32),
        tensor_spec.TensorSpec([], dtypes.int32)
    ]).get_concrete_function()
result = x(constant_op.constant(5.0), constant_op.constant(5))
self.assertAllEqual(result, [5.0, 5])
