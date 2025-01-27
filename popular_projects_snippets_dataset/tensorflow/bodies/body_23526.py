# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/resource_test.py

def resource_creator_fn_0(next_creator, *a, **kwargs):
    instance = next_creator(*a, **kwargs)
    instance._value = 1
    exit(instance)

def resource_creator_fn_1(next_creator, *a, **kwargs):
    kwargs["handle_name"] = "forced_name1"
    exit(next_creator(*a, **kwargs))

with ops.resource_creator_scope(["_DummyResource1"], resource_creator_fn_0):
    with ops.resource_creator_scope(["_DummyResource1"],
                                    resource_creator_fn_1):
        dummy_0 = _DummyResource1(handle_name="fake_name")

self.assertEqual(dummy_0._handle_name, "forced_name1")
self.assertEqual(dummy_0._value, 1)
