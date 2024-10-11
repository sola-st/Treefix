# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_v1_tensor_op_test.py
with self.cached_session() as sess:
    c = constant_op.constant(1)
    s1 = summary_lib.tensor_summary("s1", c)
    with ops.name_scope("foo", skip_on_eager=False):
        s2 = summary_lib.tensor_summary("s2", c)
        with ops.name_scope("zod", skip_on_eager=False):
            s3 = summary_lib.tensor_summary("s3", c)
            s4 = summary_lib.tensor_summary("TensorSummary", c)
    summ1, summ2, summ3, summ4 = self.evaluate([s1, s2, s3, s4])

v1 = self._SummarySingleValue(summ1)
self.assertEqual(v1.tag, "s1")

v2 = self._SummarySingleValue(summ2)
self.assertEqual(v2.tag, "foo/s2")

v3 = self._SummarySingleValue(summ3)
self.assertEqual(v3.tag, "foo/zod/s3")

v4 = self._SummarySingleValue(summ4)
self.assertEqual(v4.tag, "foo/zod/TensorSummary")
