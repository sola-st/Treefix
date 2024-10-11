# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
rt = RaggedTensor.from_row_splits(b'a b c d e f g'.split(),
                                  [0, 2, 5, 6, 6, 7])
self.assertEqual(rt.shape.as_list(), rt.get_shape().as_list())
