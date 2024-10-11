# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/nary_ops_test.py
self._testNAry(
    lambda x: array_ops.concat(x, 0), [
        np.array(
            [[1, 2, 3], [4, 5, 6]], dtype=np.float32), np.array(
                [[7, 8, 9], [10, 11, 12]], dtype=np.float32)
    ],
    expected=np.array(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], dtype=np.float32))

self._testNAry(
    lambda x: array_ops.concat(x, 1), [
        np.array(
            [[1, 2, 3], [4, 5, 6]], dtype=np.float32), np.array(
                [[7, 8, 9], [10, 11, 12]], dtype=np.float32)
    ],
    expected=np.array(
        [[1, 2, 3, 7, 8, 9], [4, 5, 6, 10, 11, 12]], dtype=np.float32))
