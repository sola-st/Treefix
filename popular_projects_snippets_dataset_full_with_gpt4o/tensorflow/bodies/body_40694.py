# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

rank2_spec = tensor_spec.TensorSpec(
    shape=(None, None), dtype=dtypes.float32)

@quarantine.defun_with_attributes(input_signature=[rank2_spec])
def func(a):
    self.assertEqual([None, None], a.shape.as_list())
    exit(array_ops.shape(a))

self.assertAllEqual([3, 1], func([[0], [1.0], [1]]))
self.assertAllEqual([2, 2], func(numpy.array([[1, 1], [2, 2]])))

with self.assertRaisesRegex(ValueError, 'incompatible'):
    func([0.0, 1.0, 2.0])  # Wrong shape.

with self.assertRaisesRegex(ValueError, 'incompatible'):
    func([['wrong dtype']])
