# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/image_ops_test.py
# The expected matrix might look uneven in terms of how many of each number
# there is, but this is an artifact of doing the dilation and convolution
# iteratively. The behavior is less esoteric in the 3x3To12x12 case below.
self._assertForwardOpMatchesExpected(
    np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=np.float32), [9, 9],
    expected=np.array(
        [[1, 1, 2, 2, 2, 2, 3, 3, 3], [1, 1, 2, 2, 2, 2, 3, 3, 3],
         [4, 4, 5, 5, 5, 5, 6, 6, 6], [4, 4, 5, 5, 5, 5, 6, 6, 6],
         [4, 4, 5, 5, 5, 5, 6, 6, 6], [4, 4, 5, 5, 5, 5, 6, 6, 6],
         [7, 7, 8, 8, 8, 8, 9, 9, 9], [7, 7, 8, 8, 8, 8, 9, 9, 9],
         [7, 7, 8, 8, 8, 8, 9, 9, 9]],
        dtype=np.float32))
