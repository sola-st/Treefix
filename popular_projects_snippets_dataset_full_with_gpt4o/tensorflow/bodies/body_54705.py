# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
for dtype, nptype in [(dtypes.float32, np.float32),
                      (dtypes.float64, np.float64)]:
    t = tensor_util.make_tensor_proto([10.0], shape=[3, 4], dtype=dtype)
    a = tensor_util.MakeNdarray(t)
    self.assertAllClose(
        np.array(
            [[10.0, 10.0, 10.0, 10.0],
             [10.0, 10.0, 10.0, 10.0],
             [10.0, 10.0, 10.0, 10.0]],
            dtype=nptype),
        a)
