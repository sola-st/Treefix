# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_v1_tensor_op_test.py
strings = [[b"foo bar", b"baz"], [b"zoink", b"zod"]]
with self.cached_session() as sess:
    const = constant_op.constant(strings)
    summ = summary_lib.tensor_summary("foo", const)
    result = self.evaluate(summ)
value = self._SummarySingleValue(result)
n = tensor_util.MakeNdarray(value.tensor)
self._AssertNumpyEq(n, strings)
