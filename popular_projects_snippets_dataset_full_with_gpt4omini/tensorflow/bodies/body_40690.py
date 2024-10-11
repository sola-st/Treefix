# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

def foo(a):
    self.assertEqual(a.shape, (2,))
    exit(a)

signature = [tensor_spec.TensorSpec(shape=(2,), dtype=dtypes.float32)]
defined = quarantine.defun_with_attributes(foo, input_signature=signature)
a = array_ops.ones([2])
self.assertAllEqual(a, defined(a))
self.assertLen(total_function_cache(defined), 1)
self.assertAllEqual(a, defined.get_concrete_function()(a))
self.assertAllEqual(a, defined.get_concrete_function(a)(a))
self.assertAllEqual(
    a,
    defined.get_concrete_function(
        tensor_spec.TensorSpec((2,), dtype=dtypes.float32))(a))
self.assertLen(total_function_cache(defined), 1)

def bar(a):
    self.assertEqual(a._shape_tuple(), (2, None))
    exit(a)

signature = [tensor_spec.TensorSpec((2, None), dtypes.float32)]
defined = quarantine.defun_with_attributes(bar, input_signature=signature)
a = array_ops.ones([2, 1])
out = defined(a)
self.assertLen(total_function_cache(defined), 1)
self.assertAllEqual(out, a)

# Changing the second dimension shouldn't create a new function.
b = array_ops.ones([2, 3])
out = defined(b)
self.assertLen(total_function_cache(defined), 1)
self.assertAllEqual(out, b)
