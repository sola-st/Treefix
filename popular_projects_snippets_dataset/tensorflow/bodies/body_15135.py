# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
rt = RaggedTensor.from_tensor([[[1], [2], [3]], [[4], [5], [6]]],
                              ragged_rank=1)
self.assertEqual(rt.shape.as_list(), [2, 3, 1])
with self.assertRaises(ValueError):
    rt._set_shape([None, None, 5])
with self.assertRaisesRegex(ValueError, 'Inconsistent size'):
    rt._set_shape([None, 5, None])
with self.assertRaises(ValueError):
    rt._set_shape([5, None, None])
