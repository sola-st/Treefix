# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/lang/special_functions_test.py
self.assertEqual(special_functions.stack(1, strict=False), 1)
self.assertListEqual(
    special_functions.stack([1, 2, 3], strict=False), [1, 2, 3])
# TODO(mdan): This should probably forward to tf.stack.
self.assertTrue(
    isinstance(
        special_functions.stack(
            [constant_op.constant(1),
             constant_op.constant(2)], strict=False), list))

with self.assertRaises(ValueError):
    special_functions.stack([1, 2, 3])

t = constant_op.constant([1.0, 2.0])
l = list_ops.tensor_list_from_tensor(
    t, element_shape=constant_op.constant([], dtype=dtypes.int32))
self.assertTrue(
    tensor_util.is_tf_type(
        special_functions.stack(l, element_dtype=dtypes.float32)))
