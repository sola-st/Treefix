# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops_test.py
st = StructuredTensor.from_pyval(values)
# NOTE: rank is very robust. There aren't arguments that
# should cause this operation to fail.
actual = array_ops.rank(st)
self.assertAllEqual(expected, actual)
