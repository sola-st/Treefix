# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
for dtype in standard_dtypes:
    if dtype == bfloat16 or dtype == np.complex128:
        continue
    # NV FP8 not supported on TPU.
    if (dtype in [float8_e4m3fn, float8_e5m2] and
        self.backend.platform == "tpu"):
        continue
    arr = self.backend.buffer_from_pyval(np.array([0, 1], dtype))
    arr = np.asarray(arr)
    self.assertEqual(dtype, type(arr[0]))
