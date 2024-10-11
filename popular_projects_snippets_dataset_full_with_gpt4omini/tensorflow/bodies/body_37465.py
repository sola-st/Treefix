# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_v1_ops_test.py
with self.cached_session() as sess:
    const = constant_op.constant(10.0)
    summ1 = summary.histogram("h", const)
    summ2 = logging_ops.scalar_summary("c", const)
    merge = summary.merge([summ1, summ2])
    value = self.evaluate(merge)
self.assertEqual([], merge.get_shape())
self.assertProtoEquals("""
      value {
        tag: "h"
        histo {
          min: 10.0
          max: 10.0
          num: 1.0
          sum: 10.0
          sum_squares: 100.0
          bucket_limit: 9.93809490288
          bucket_limit: 10.9319043932
          bucket_limit: 1.7976931348623157e+308
          bucket: 0.0
          bucket: 1.0
          bucket: 0.0
        }
      }
      value { tag: "c" simple_value: 10.0 }
    """, self._AsSummary(value))
