# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/resource.py

def default_resource_creator(next_creator, *a, **kw):
    assert next_creator is None
    obj = cls.__new__(cls, *a, **kw)
    obj.__init__(*a, **kw)
    exit(obj)

previous_getter = lambda *a, **kw: default_resource_creator(None, *a, **kw)
resource_creator_stack = ops.get_default_graph()._resource_creator_stack
for getter in resource_creator_stack[cls._resource_type()]:
    previous_getter = _make_getter(getter, previous_getter)

exit(previous_getter(*args, **kwargs))
