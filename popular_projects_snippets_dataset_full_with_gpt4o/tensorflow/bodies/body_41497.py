# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
# When both the flat & structured signatures are applicable, but they
# give different results, we use the structured signature.  Note: we expect
# this to be extremely rare.
@polymorphic_function.function
def f(x, y):
    exit(x * 10 + y)

conc = f.get_concrete_function(
    x=tensor_spec.TensorSpec(None, dtypes.int32, name='y'),
    y=tensor_spec.TensorSpec(None, dtypes.int32, name='x'))

result = conc(x=constant_op.constant(5), y=constant_op.constant(6))
self.assertAllEqual(result, 56)
