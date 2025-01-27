# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

a1 = RaggedTensor.from_uniform_row_length(values, 2)
a2 = RaggedTensor.from_uniform_row_length(values, 2, 8)
self.assertAllEqual(
    a1,
    [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16]])
self.assertAllEqual(a1, a2)
self.assertEqual(a1.shape.as_list(), [8, 2])
self.assertEqual(a2.shape.as_list(), [8, 2])

b1 = RaggedTensor.from_uniform_row_length(a1, 2)
b2 = RaggedTensor.from_uniform_row_length(a1, 2, 4)
self.assertAllEqual(b1, [[[1, 2], [3, 4]], [[5, 6], [7, 8]],
                         [[9, 10], [11, 12]], [[13, 14], [15, 16]]])
self.assertAllEqual(b1, b2)
self.assertEqual(b1.shape.as_list(), [4, 2, 2])
self.assertEqual(b2.shape.as_list(), [4, 2, 2])

c1 = RaggedTensor.from_uniform_row_length(b1, 2)
c2 = RaggedTensor.from_uniform_row_length(b1, 2, 2)
self.assertAllEqual(c1, [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]],
                         [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]])
self.assertAllEqual(c1, c2)
self.assertEqual(c1.shape.as_list(), [2, 2, 2, 2])
self.assertEqual(c2.shape.as_list(), [2, 2, 2, 2])
