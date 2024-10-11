# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_v1_ops_test.py
with self.cached_session() as sess:
    const = constant_op.constant([10.0, 20.0])
    summ = logging_ops.scalar_summary(["c1", "c2"], const)
    value = self.evaluate(summ)
self.assertEqual([], summ.get_shape())
self.assertProtoEquals("""
      value { tag: "c1" simple_value: 10.0 }
      value { tag: "c2" simple_value: 20.0 }
      """, self._AsSummary(value))
