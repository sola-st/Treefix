# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
my_collection_name = '__updates__'
_, update_op = metrics.mean_iou(
    predictions=array_ops.ones([10, 1]),
    labels=array_ops.ones([10, 1]),
    num_classes=2,
    updates_collections=[my_collection_name])
self.assertListEqual(ops.get_collection(my_collection_name), [update_op])
