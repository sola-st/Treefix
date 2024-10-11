# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/unary_ops_test.py
types = {
    dtypes.bool, dtypes.float32, dtypes.float64, dtypes.complex64,
    dtypes.int32, dtypes.int64, dtypes.uint32, dtypes.uint64
}
for src_type in types:
    for dst_type in types:
        self._testCast(src_type, dst_type)
