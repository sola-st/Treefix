# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
my_collection_name = '__metrics__'
prec, _ = metrics.precision_at_thresholds(
    predictions=array_ops.ones((10, 1)),
    labels=array_ops.ones((10, 1)),
    thresholds=[0, 0.5, 1.0],
    metrics_collections=[my_collection_name])
rec, _ = metrics.recall_at_thresholds(
    predictions=array_ops.ones((10, 1)),
    labels=array_ops.ones((10, 1)),
    thresholds=[0, 0.5, 1.0],
    metrics_collections=[my_collection_name])
self.assertListEqual(ops.get_collection(my_collection_name), [prec, rec])
