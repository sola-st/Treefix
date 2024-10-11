# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
my_collection_name = '__metrics__'
mean_accuracy, _ = metrics.mean_per_class_accuracy(
    predictions=array_ops.ones([10, 1]),
    labels=array_ops.ones([10, 1]),
    num_classes=2,
    metrics_collections=[my_collection_name])
self.assertListEqual(
    ops.get_collection(my_collection_name), [mean_accuracy])
