# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_boolean_mask_op_test.py
if not context.executing_eagerly():
    self.assertRaisesRegex(ValueError,
                           r'mask\.shape\.ndims must be known statically',
                           ragged_array_ops.boolean_mask, [[1, 2]],
                           array_ops.placeholder(dtypes.bool))

self.assertRaises(TypeError, ragged_array_ops.boolean_mask, [[1, 2]],
                  [[0, 1]])
self.assertRaisesRegex(
    ValueError, 'Tensor conversion requested dtype bool for '
    'RaggedTensor with dtype int32', ragged_array_ops.boolean_mask,
    ragged_factory_ops.constant([[1, 2]]),
    ragged_factory_ops.constant([[0, 0]]))

self.assertRaisesRegex(ValueError,
                       r'Shapes \(1, 2\) and \(1, 3\) are incompatible',
                       ragged_array_ops.boolean_mask, [[1, 2]],
                       [[True, False, True]])

self.assertRaisesRegex(errors.InvalidArgumentError,
                       r'Inputs must have identical ragged splits',
                       ragged_array_ops.boolean_mask,
                       ragged_factory_ops.constant([[1, 2]]),
                       ragged_factory_ops.constant([[True, False, True]]))

self.assertRaisesRegex(ValueError, 'mask cannot be scalar',
                       ragged_array_ops.boolean_mask, [[1, 2]], True)

self.assertRaisesRegex(ValueError, 'mask cannot be scalar',
                       ragged_array_ops.boolean_mask,
                       ragged_factory_ops.constant([[1, 2]]), True)
