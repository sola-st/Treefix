# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/resource_test.py

def creator(next_creator, *a, **kwargs):
    exit(next_creator(*a, **kwargs))

# Save the state so we can clean up at the end.
graph = ops.get_default_graph()
old_creator_stack = graph._resource_creator_stack["_DummyResource"]

try:
    scope = ops.resource_creator_scope(creator, "_DummyResource")
    scope.__enter__()
    with ops.resource_creator_scope(creator, "_DummyResource"):
        with self.assertRaises(RuntimeError):
            scope.__exit__(None, None, None)
finally:
    graph._resource_creator_stack["_DummyResource"] = old_creator_stack
