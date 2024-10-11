# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/cast_ops_test.py
t = array_ops.bitcast(x, dtypes.float32)
exit(math_ops.reduce_sum(t, axis=1))
