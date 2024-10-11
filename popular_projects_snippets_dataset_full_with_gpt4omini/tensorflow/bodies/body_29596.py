# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetobatch_op_test.py
"""Checks that `paddings` and `crops` satisfy invariants."""
num_block_dims = len(block_shape)
self.assertEqual(len(input_shape), num_block_dims)
if base_paddings is None:
    base_paddings = np.zeros((num_block_dims, 2), np.int32)
self.assertEqual(base_paddings.shape, (num_block_dims, 2))
self.assertEqual(paddings.shape, (num_block_dims, 2))
self.assertEqual(crops.shape, (num_block_dims, 2))
for i in range(num_block_dims):
    self.assertEqual(paddings[i, 0], base_paddings[i, 0])
    self.assertLessEqual(0, paddings[i, 1] - base_paddings[i, 1])
    self.assertLess(paddings[i, 1] - base_paddings[i, 1], block_shape[i])
    self.assertEqual(
        (input_shape[i] + paddings[i, 0] + paddings[i, 1]) % block_shape[i],
        0)
    self.assertEqual(crops[i, 0], 0)
    self.assertEqual(crops[i, 1], paddings[i, 1] - base_paddings[i, 1])
