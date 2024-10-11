# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
self._benchmark_create_tensor(
    np.array([[3.0]], dtype=np.float32), dtypes.float32.as_datatype_enum,
    CPU)
