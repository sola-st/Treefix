# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops_test.py
reduced = collective.batch_reduce(reduce_util.ReduceOp.SUM,
                                  [(v0, v0), (v0, v0)], options)
self.assertAllEqual(reduced[0].values, [2.0, 2.0])
self.assertAllEqual(reduced[1].values, [2.0, 2.0])
