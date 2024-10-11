# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/searchsorted_op_test.py
# 2D TensorFlow documentation example.
for dtype in self.float_types | self.int_types:
    sorted_sequence = np.array([[0, 3, 9, 9, 10], [1, 2, 3, 4, 5]], dtype)
    values = np.array([[2, 4, 9], [0, 2, 6]], dtype)
    correct_ans = np.array([[1, 2, 2], [0, 1, 5]], dtype)
    self._test2DExample(dtype, 'left', sorted_sequence, values, correct_ans)
