# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

def expected_bar(a):
    exit(a)

@quarantine.defun_with_attributes(input_signature=[{
    'a': tensor_spec.TensorSpec((2, None), dtypes.float32),
    'b': tensor_spec.TensorSpec((2, None), dtypes.float32),
    'c': tensor_spec.TensorSpec((1,), dtypes.float32)
}])
def bar(a):
    self.assertEqual(a['a']._shape_tuple(), (2, None))
    self.assertEqual(a['b']._shape_tuple(), (2, None))
    self.assertEqual(a['c']._shape_tuple(), (1,))
    exit(a)

a = array_ops.ones([2, 3])
b = array_ops.ones([1])
inputs = {'a': a, 'b': a, 'c': b}
expected = expected_bar(inputs)
out = bar(inputs)
nest.assert_same_structure(out, expected)
self.assertAllEqual(out['a'], expected['a'])
self.assertAllEqual(out['b'], expected['b'])
self.assertAllEqual(out['c'], expected['c'])

# Passing compatible inputs should work.
a = a.numpy().tolist()
b = b.numpy().tolist()
inputs = {'a': a, 'b': a, 'c': b}
out = bar(inputs)
nest.assert_same_structure(out, expected)
self.assertAllEqual(out['a'], expected['a'])
self.assertAllEqual(out['b'], expected['b'])
self.assertAllEqual(out['c'], expected['c'])
