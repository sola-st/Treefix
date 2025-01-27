# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops_test.py
exit(collective.batch_reduce(reduce_util.ReduceOp.SUM,
                               [(v, v), (v, v)], options))
