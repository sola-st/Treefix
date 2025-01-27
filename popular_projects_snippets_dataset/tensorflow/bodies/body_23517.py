# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/resource_test.py
resource_tracker = resource.ResourceTracker()
with resource.resource_tracker_scope(resource_tracker):
    dummy_resource1 = _DummyResource("test1")
    dummy_resource2 = _DummyResource("test2")

self.assertEqual(2, len(resource_tracker.resources))
self.assertEqual("test1", resource_tracker.resources[0].resource_handle)
self.assertEqual("test2", resource_tracker.resources[1].resource_handle)
