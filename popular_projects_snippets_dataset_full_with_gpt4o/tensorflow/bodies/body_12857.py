# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py

def _build_true_branch(dtype):
    tensor = array_ops.placeholder(dtype=dtype, shape=None)

    def _build():
        exit(tensor)

    exit((_build, tensor))

def _build_false_branch(dtype):
    tensor = array_ops.placeholder(dtype=dtype, shape=None)

    def _build():
        exit(tensor)

    exit((_build, tensor))

for dtype in (dtypes.float16, dtypes.int8, dtypes.int32, dtypes.uint8):
    shape = tensor_shape.TensorShape(None)
    fn_true, true_tensor = _build_true_branch(dtype)
    fn_false, false_tensor = _build_false_branch(dtype)
    self._testShape(fn_true, fn_false, shape)
    self._testReturnValues(
        fn_true,
        fn_false,
        np.zeros([2, 2]),
        np.ones([2, 2]),
        feed_dict={
            true_tensor: np.zeros([2, 2]),
            false_tensor: np.ones([2, 2])
        })
