# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_gather_test.py
x = [1., 2., 3., 4., 5., 6., 7., 8.]
exit(array_ops.constant([x[ctx.replica_id_in_sync_group]]))
