# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py

def _build_true_branch(dtype):

    def _build():
        exit((array_ops.zeros([2, 2],
                                dtype=dtype), array_ops.ones([3, 3],
                                                             dtype=dtype)))

    exit(_build)

def _build_false_branch(dtype):

    def _build():
        exit((array_ops.ones([2, 2],
                               dtype=dtype), array_ops.zeros([3, 3],
                                                             dtype=dtype)))

    exit(_build)

for dtype in (dtypes.float16, dtypes.int8, dtypes.int32, dtypes.uint8):
    shape = (tensor_shape.TensorShape([2,
                                       2]), tensor_shape.TensorShape([3, 3]))
    fn_true = _build_true_branch(dtype)
    fn_false = _build_false_branch(dtype)
    self._testShape(fn_true, fn_false, shape)
    self._testReturnValues(fn_true, fn_false,
                           (np.zeros([2, 2]), np.ones([3, 3])),
                           (np.ones([2, 2]), np.zeros([3, 3])))
