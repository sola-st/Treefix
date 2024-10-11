# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
my_collection_name = '__metrics__'
mean, _ = metrics.mean_tensor(
    array_ops.ones([4, 3]), metrics_collections=[my_collection_name])
self.assertListEqual(ops.get_collection(my_collection_name), [mean])
