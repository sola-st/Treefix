# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_v1_tensor_op_test.py
with self.cached_session() as sess:
    const = array_ops.ones([5, 5, 5])
    summ = summary_lib.tensor_summary("foo", const)
    result = self.evaluate(summ)
value = self._SummarySingleValue(result)
n = tensor_util.MakeNdarray(value.tensor)
self._AssertNumpyEq(n, np.ones([5, 5, 5]))
