# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
array_transforms = [
    lambda x: x,  # Identity,
    ops.convert_to_tensor,
    np.array,
    lambda x: np.array(x, dtype=np.float32),
    lambda x: np.array(x, dtype=np.float64),
    np_array_ops.array,
    lambda x: np_array_ops.array(x, dtype=np.float32),
    lambda x: np_array_ops.array(x, dtype=np.float64)
]

def run_test(arr):
    for fn in array_transforms:
        arr = fn(arr)
        self.match(
            np_array_ops.diag(arr), np.diag(arr), msg='diag({})'.format(arr))
        for k in range(-3, 3):
            self.match(
                np_array_ops.diag(arr, k),
                np.diag(arr, k),
                msg='diag({}, k={})'.format(arr, k))

    # 2-d arrays.
run_test(np.arange(9).reshape((3, 3)).tolist())
run_test(np.arange(6).reshape((2, 3)).tolist())
run_test(np.arange(6).reshape((3, 2)).tolist())
run_test(np.arange(3).reshape((1, 3)).tolist())
run_test(np.arange(3).reshape((3, 1)).tolist())
run_test([[5]])
run_test([[]])
run_test([[], []])

# 1-d arrays.
run_test([])
run_test([1])
run_test([1, 2])
