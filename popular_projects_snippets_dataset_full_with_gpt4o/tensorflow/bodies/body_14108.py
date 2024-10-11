# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops_test.py
st = StructuredTensor.from_pyval(values)
# NOTE: size is very robust. There aren't arguments that
# should cause this operation to fail.
actual = array_ops.size(st, out_type=dtype)
self.assertAllEqual(actual, expected)

actual2 = array_ops.size_v2(st, out_type=dtype)
self.assertAllEqual(actual2, expected)
