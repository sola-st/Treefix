# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def f(x, y):
    exit((x, y))

f(constant_op.constant([[3., 4.]]), constant_op.constant([2.]))
f(constant_op.constant([[3, 4, 5]]), constant_op.constant([2]))

signatures_args = set()
concrete_functions = f._list_all_concrete_functions_for_serialization()
for concrete_function in concrete_functions:
    args, kwargs = concrete_function.structured_input_signature
    signatures_args.add(args)
    self.assertEqual(dict(), kwargs)

self.assertEqual(
    signatures_args,
    set(((tensor_spec.TensorSpec([1, 2], dtypes.float32, name='x'),
          tensor_spec.TensorSpec([1], dtypes.float32, name='y')),
         (tensor_spec.TensorSpec([1, 3], dtypes.int32, name='x'),
          tensor_spec.TensorSpec([1], dtypes.int32, name='y')))))
