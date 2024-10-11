# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
self._benchmark_create_tensor(
    np.array([[3]], dtype=np.int32), dtypes.int32.as_datatype_enum, CPU)
