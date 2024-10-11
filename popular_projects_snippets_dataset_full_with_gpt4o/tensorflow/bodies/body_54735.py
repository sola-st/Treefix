# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
for dtype, np_dtype in [(dtypes.complex64, np.complex64),
                        (dtypes.complex128, np.complex128)]:
    t = tensor_util.make_tensor_proto((1 + 1j), shape=[3, 4], dtype=dtype)
    a = tensor_util.MakeNdarray(t)
    self.assertAllClose(
        np.array(
            [[(1 + 1j), (1 + 1j), (1 + 1j), (1 + 1j)],
             [(1 + 1j), (1 + 1j), (1 + 1j), (1 + 1j)],
             [(1 + 1j), (1 + 1j), (1 + 1j), (1 + 1j)]],
            dtype=np_dtype),
        a)
