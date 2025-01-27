# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/nary_ops_test.py
# Tests cases where input shape is empty.
self._testNAry(lambda x: array_ops.strided_slice_grad(*x),
               [np.array([], dtype=np.int32),
                np.array([], dtype=np.int32),
                np.array([], dtype=np.int32),
                np.array([], dtype=np.int32),
                np.float32(0.5)],
               expected=np.array(np.float32(0.5), dtype=np.float32))

# Tests case where input shape is non-empty, but gradients are empty.
self._testNAry(lambda x: array_ops.strided_slice_grad(*x),
               [np.array([3], dtype=np.int32),
                np.array([0], dtype=np.int32),
                np.array([0], dtype=np.int32),
                np.array([1], dtype=np.int32),
                np.array([], dtype=np.float32)],
               expected=np.array([0, 0, 0], dtype=np.float32))

self._testNAry(lambda x: array_ops.strided_slice_grad(*x),
               [np.array([3, 0], dtype=np.int32),
                np.array([1, 0], dtype=np.int32),
                np.array([3, 0], dtype=np.int32),
                np.array([1, 1], dtype=np.int32),
                np.array([[], []], dtype=np.float32)],
               expected=np.array([[], [], []], dtype=np.float32))

self._testNAry(lambda x: array_ops.strided_slice_grad(*x),
               [np.array([3, 3], dtype=np.int32),
                np.array([1, 1], dtype=np.int32),
                np.array([3, 3], dtype=np.int32),
                np.array([1, 1], dtype=np.int32),
                np.array([[5, 6], [8, 9]], dtype=np.float32)],
               expected=np.array([[0, 0, 0], [0, 5, 6], [0, 8, 9]],
                                 dtype=np.float32))

def ssg_test(x):
    exit(array_ops.strided_slice_grad(*x, shrink_axis_mask=0x4,
                                        new_axis_mask=0x1))

self._testNAry(ssg_test,
               [np.array([3, 1, 3], dtype=np.int32),
                np.array([0, 0, 0, 2], dtype=np.int32),
                np.array([0, 3, 1, -4], dtype=np.int32),
                np.array([1, 2, 1, -3], dtype=np.int32),
                np.array([[[1], [2]]], dtype=np.float32)],
               expected=np.array([[[0, 0, 1]], [[0, 0, 0]], [[0, 0, 2]]],
                                 dtype=np.float32))

ssg_test2 = lambda x: array_ops.strided_slice_grad(*x, new_axis_mask=0x15)
self._testNAry(ssg_test2,
               [np.array([4, 4], dtype=np.int32),
                np.array([0, 0, 0, 1, 0], dtype=np.int32),
                np.array([0, 3, 0, 4, 0], dtype=np.int32),
                np.array([1, 2, 1, 2, 1], dtype=np.int32),
                np.array([[[[[1], [2]]], [[[3], [4]]]]], dtype=np.float32)],
               expected=np.array([[0, 1, 0, 2], [0, 0, 0, 0], [0, 3, 0, 4],
                                  [0, 0, 0, 0]], dtype=np.float32))

self._testNAry(lambda x: array_ops.strided_slice_grad(*x),
               [np.array([3, 3], dtype=np.int32),
                np.array([0, 2], dtype=np.int32),
                np.array([2, 0], dtype=np.int32),
                np.array([1, -1], dtype=np.int32),
                np.array([[1, 2], [3, 4]], dtype=np.float32)],
               expected=np.array([[0, 2, 1], [0, 4, 3], [0, 0, 0]],
                                 dtype=np.float32))

self._testNAry(lambda x: array_ops.strided_slice_grad(*x),
               [np.array([3, 3], dtype=np.int32),
                np.array([2, 2], dtype=np.int32),
                np.array([0, 1], dtype=np.int32),
                np.array([-1, -2], dtype=np.int32),
                np.array([[1], [2]], dtype=np.float32)],
               expected=np.array([[0, 0, 0], [0, 0, 2], [0, 0, 1]],
                                 dtype=np.float32))
