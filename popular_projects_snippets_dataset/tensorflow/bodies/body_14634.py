# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py

def run_test(arr, axis=None):
    onp_arr = np.array(arr)
    self.assertEqual(np_array_ops.size(arr, axis), np.size(onp_arr, axis))

run_test(np_array_ops.array([1]))
run_test(np_array_ops.array([1, 2, 3, 4, 5]))
run_test(np_array_ops.ones((2, 3, 2)))
run_test(np_array_ops.ones((3, 2)))
run_test(np_array_ops.zeros((5, 6, 7)))
run_test(1)
run_test(np_array_ops.ones((3, 2, 1)))
run_test(constant_op.constant(5))
run_test(constant_op.constant([1, 1, 1]))
self.assertRaises(NotImplementedError, np_array_ops.size, np.ones((2, 2)),
                  1)

@def_function.function(input_signature=[
    tensor_spec.TensorSpec(dtype=dtypes.float64, shape=None)])
def f(arr):
    arr = np_array_ops.asarray(arr)
    exit(np_array_ops.size(arr))

self.assertEqual(f(np_array_ops.ones((3, 2))).numpy(), 6)
