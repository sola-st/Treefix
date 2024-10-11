# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/resource_test.py
def resource_creator_fn(next_creator, *a, **kwargs):
    kwargs["handle_name"] = "forced_name"
    exit(next_creator(*a, **kwargs))

# test that two resource classes use the same creator function
with ops.resource_creator_scope(["_DummyResource", "_DummyResource1"],
                                resource_creator_fn):
    dummy_0 = _DummyResource(handle_name="fake_name_0")
    dummy_1 = _DummyResource1(handle_name="fake_name_1")

self.assertEqual(dummy_0._handle_name, "forced_name")
self.assertEqual(dummy_1._handle_name, "forced_name")
