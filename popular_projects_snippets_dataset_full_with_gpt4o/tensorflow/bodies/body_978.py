# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/unary_ops_test.py
fp8_types = {dtypes.float8_e5m2, dtypes.float8_e4m3fn}
# TODO(b/259609697): Test casting to bool. Casting from float8 to bool is
# currently not supported since the cast is lowered to an Ne (not-equal) op,
# and FP8 is currently not supported with Ne.
other_types = {
    dtypes.float32, dtypes.float64, dtypes.complex64,
    dtypes.int32, dtypes.int64, dtypes.uint32, dtypes.uint64
}
for fp8_type in fp8_types:
    for other_type in other_types | fp8_types:
        self._testCast(fp8_type, other_type)
        self._testCast(other_type, fp8_type)
