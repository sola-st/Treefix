# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/lang/special_functions_test.py
elements = [constant_op.constant([1, 2]), constant_op.constant([3, 4])]

l = special_functions.tensor_list(elements, use_tensor_array=True)
sl = l.stack()
with self.cached_session() as sess:
    self.assertAllEqual(self.evaluate(sl), [[1, 2], [3, 4]])
