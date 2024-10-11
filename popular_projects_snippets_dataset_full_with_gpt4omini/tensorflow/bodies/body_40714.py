# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

def f(rt):
    self.assertEqual(rt.values.shape.as_list(), [None])
    self.assertEqual(rt.row_splits.shape.as_list(), [4])
    exit(rt)

signature = [
    ragged_tensor.RaggedTensorSpec(shape=[3, None], dtype=dtypes.int32)
]
defined = quarantine.defun_with_attributes(f, input_signature=signature)
rt1 = ragged_factory_ops.constant([[1], [], [2, 3, 4]])
out1 = defined(rt1)
self.assertLen(total_function_cache(defined), 1)
self.assertAllEqual(out1.values, rt1.values)
self.assertAllEqual(out1.row_splits, rt1.row_splits)

# Changing the row lengths shouldn't create a new function.
rt2 = ragged_factory_ops.constant([[1, 2], [3, 4], [5]])
out2 = defined(rt2)
self.assertLen(total_function_cache(defined), 1)
self.assertAllEqual(out2.values, rt2.values)
self.assertAllEqual(out2.row_splits, rt2.row_splits)

# Different number of rows
rt3 = ragged_factory_ops.constant([[1, 2], [3, 4], [5], [6]])
with self.assertRaisesRegex(ValueError, 'incompatible'):
    defined(rt3)

# Different dtype
rt4 = ragged_factory_ops.constant([[1.0, 2.0], [], [3.0]])
with self.assertRaisesRegex(ValueError, 'Structure .* does not match'):
    defined(rt4)

# Different rank
rt5 = ragged_factory_ops.constant([[[1]], [[2]], [[3]]])
with self.assertRaisesRegex(ValueError, 'does not match'):
    defined(rt5)
