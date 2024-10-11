# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
my_collection_name = '__metrics__'
mean, _ = metrics.sensitivity_at_specificity(
    predictions=array_ops.ones((10, 1)),
    labels=array_ops.ones((10, 1)),
    specificity=0.7,
    metrics_collections=[my_collection_name])
self.assertListEqual(ops.get_collection(my_collection_name), [mean])
