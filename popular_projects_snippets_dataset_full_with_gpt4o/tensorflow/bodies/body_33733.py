# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
my_collection_name = '__updates__'
_, precision_op = metrics.precision_at_thresholds(
    predictions=array_ops.ones((10, 1)),
    labels=array_ops.ones((10, 1)),
    thresholds=[0, 0.5, 1.0],
    updates_collections=[my_collection_name])
_, recall_op = metrics.recall_at_thresholds(
    predictions=array_ops.ones((10, 1)),
    labels=array_ops.ones((10, 1)),
    thresholds=[0, 0.5, 1.0],
    updates_collections=[my_collection_name])
self.assertListEqual(
    ops.get_collection(my_collection_name), [precision_op, recall_op])
