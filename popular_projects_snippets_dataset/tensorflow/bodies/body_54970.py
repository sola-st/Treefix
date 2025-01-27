# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/versions_test.py
version = versions.GRAPH_DEF_VERSION
min_consumer = versions.GRAPH_DEF_VERSION_MIN_CONSUMER
min_producer = versions.GRAPH_DEF_VERSION_MIN_PRODUCER
for v in version, min_consumer, min_producer:
    self.assertEqual(type(v), int)
self.assertLessEqual(0, min_consumer)
self.assertLessEqual(0, min_producer)
self.assertLessEqual(min_producer, version)
