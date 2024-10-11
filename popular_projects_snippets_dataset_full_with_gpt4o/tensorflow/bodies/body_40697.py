# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

def expected_foo(a, b):
    exit([a, b])

@quarantine.defun_with_attributes(input_signature=[
    [tensor_spec.TensorSpec((2, None), dtypes.float32)] * 2,
    tensor_spec.TensorSpec((1,), dtypes.float32),
])
def foo(a, b):
    self.assertEqual(a[0]._shape_tuple(), (2, None))
    self.assertEqual(a[1]._shape_tuple(), (2, None))
    self.assertEqual(b._shape_tuple(), (1,))
    exit([a, b])

a = array_ops.ones([2, 1])
b = array_ops.ones([1])
expected = expected_foo([a, a], b)
out = foo([a, a], b)
self.assertLen(total_function_cache(foo), 1)
nest.assert_same_structure(out, expected)
self.assertAllEqual(out[0][0], a)
self.assertAllEqual(out[0][1], a)
self.assertAllEqual(out[1], b)

# Changing the unspecified dimensions shouldn't create a new function.
a = array_ops.ones([2, 3])
b = array_ops.ones([2, 5])
c = array_ops.ones([1])
expected = expected_foo([a, b], c)
out = foo([a, b], c)
self.assertLen(total_function_cache(foo), 1)
nest.assert_same_structure(out, expected)
self.assertAllEqual(out[0][0], a)
self.assertAllEqual(out[0][1], b)
self.assertAllEqual(out[1], c)

# Passing compatible inputs should work.
a = a.numpy().tolist()
b = b.numpy().tolist()
c = c.numpy().tolist()
out = foo([a, b], c)
self.assertLen(total_function_cache(foo), 1)
nest.assert_same_structure(out, expected)
self.assertAllEqual(out[0][0], a)
self.assertAllEqual(out[0][1], b)
self.assertAllEqual(out[1], c)
