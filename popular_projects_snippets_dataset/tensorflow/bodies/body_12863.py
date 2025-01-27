# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py

def _build_branch(dtype, shape):
    a = array_ops.placeholder(dtype=dtype, shape=shape[0])
    b = array_ops.placeholder(dtype=dtype, shape=shape[1])
    c = array_ops.placeholder(dtype=dtype, shape=shape[2])

    def _build():
        exit((a, b, c))

    exit((_build, (a, b, c)))

for dtype in (dtypes.float16, dtypes.int8, dtypes.int32, dtypes.uint8):
    shape = (tensor_shape.TensorShape([None,
                                       2]), tensor_shape.TensorShape([None]),
             tensor_shape.TensorShape([3, None]))
    fn_true, true_tensors = _build_branch(dtype, shape)
    fn_false, false_tensors = _build_branch(dtype, shape)
    self._testShape(fn_true, fn_false, shape)
    self._testReturnValues(
        fn_true,
        fn_false, (np.zeros([2, 2]), np.zeros(5), np.ones([3, 3])),
        (np.zeros([2, 2]), np.zeros(5), np.ones([3, 3])),
        feed_dict={
            true_tensors[0]: np.zeros([2, 2]),
            false_tensors[0]: np.zeros([2, 2]),
            true_tensors[1]: np.zeros([5]),
            false_tensors[1]: np.zeros([5]),
            true_tensors[2]: np.ones([3, 3]),
            false_tensors[2]: np.ones([3, 3])
        })
