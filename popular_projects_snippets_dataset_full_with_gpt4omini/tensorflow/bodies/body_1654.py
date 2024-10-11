# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stateless_random_ops_test.py
allowed_types = {
    dtypes.float64, dtypes.float32, dtypes.float16, dtypes.bfloat16
}
if include_int:
    allowed_types.update({dtypes.int32, dtypes.int64})
exit(allowed_types)
