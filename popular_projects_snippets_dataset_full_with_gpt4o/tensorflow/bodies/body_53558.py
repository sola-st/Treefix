# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""EXPERIMENTAL: A context manager for setting attributes on operators.

    This context manager can be used to add additional
    attributes to operators within the scope of the context.

    For example:

       with ops.Graph().as_default() as g:
         f_1 = Foo()  # No extra attributes
         with g._attr_scope({"_a": tf.attr_value_pb2.AttrValue(b=False)}):
           f_2 = Foo()  # Additional attribute _a=False
           with g._attr_scope({"_a": tf.attr_value_pb2.AttrValue(b=True)}):
             f_3 = Foo()  # Additional attribute _a=False
             with g._attr_scope({"_a": None}):
               f_4 = Foo()  # No additional attributes.

    Args:
      attr_map: A dictionary mapping attr name strings to AttrValue protocol
        buffers or None.

    Returns:
      A context manager that sets the kernel label to be used for one or more
      ops created in that context.

    Raises:
      TypeError: If attr_map is not a dictionary mapping
        strings to AttrValue protobufs.
    """
if not isinstance(attr_map, dict):
    raise TypeError("attr_map must be a dictionary mapping "
                    "strings to AttrValue protocol buffers")
# The saved_attrs dictionary stores any currently-set labels that
# will be overridden by this context manager.
saved_attrs = {}
# Install the given attribute
for name, attr in attr_map.items():
    if not (isinstance(name, str) and
            (isinstance(attr, (type(None), attr_value_pb2.AttrValue)) or
             callable(attr))):
        raise TypeError("attr_map must be a dictionary mapping "
                        "strings to AttrValue protocol buffers or "
                        "callables that emit AttrValue protocol buffers")
    try:
        saved_attrs[name] = self._attr_scope_map[name]
    except KeyError:
        pass
    if attr is None:
        del self._attr_scope_map[name]
    else:
        self._attr_scope_map[name] = attr
try:
    exit()  # The code within the context runs here.
finally:
    # Remove the attributes set for this context, and restore any saved
    # attributes.
    for name, attr in attr_map.items():
        try:
            self._attr_scope_map[name] = saved_attrs[name]
        except KeyError:
            del self._attr_scope_map[name]
