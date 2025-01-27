# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_v1_tensor_op_test.py
s = b"foobar"
with self.cached_session() as sess:
    const = constant_op.constant(s)
    summ = summary_lib.tensor_summary("foo", const)
    result = self.evaluate(summ)

value = self._SummarySingleValue(result)
n = tensor_util.MakeNdarray(value.tensor)
self._AssertNumpyEq(n, s)
