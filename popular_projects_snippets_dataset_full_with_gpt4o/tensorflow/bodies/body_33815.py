# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
my_collection_name = '__metrics__'
mean, _ = metrics.mean_cosine_distance(
    predictions=array_ops.ones((10, 3)),
    labels=array_ops.ones((10, 3)),
    dim=1,
    metrics_collections=[my_collection_name])
self.assertListEqual(ops.get_collection(my_collection_name), [mean])
