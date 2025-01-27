# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function.py
"""Parses **kwargs into a node's attributes."""
attrs = {}

noinline = kwargs.pop("noinline", None)
if noinline is not None:
    attrs["_noinline"] = attr_value_pb2.AttrValue(b=bool(noinline))

# For compatibility with previous behavior, Defun does not perform shape
# inference through its function call operations.
attrs["_disable_call_shape_inference"] = attr_value_pb2.AttrValue(b=True)

compiled = kwargs.pop("compiled", None)
separate_compiled_gradients = kwargs.pop("separate_compiled_gradients", None)
if compiled is not None:
    attrs["_XlaCompile"] = attr_value_pb2.AttrValue(b=bool(compiled))
    attrs["_XlaSeparateCompiledGradients"] = attr_value_pb2.AttrValue(
        b=bool(separate_compiled_gradients))
    # Forward _XlaScope from enclosing context (if set), otherwise create new.
    # pylint: disable=protected-access
    if "_XlaScope" in ops.get_default_graph()._attr_scope_map:
        attrs["_XlaScope"] = ops.get_default_graph()._attr_scope_map["_XlaScope"]
    else:
        attrs["_XlaScope"] = attr_value_pb2.AttrValue(
            s=("function_%s" % func_name).encode())
    # pylint: enable=protected-access

kwargs_keys = list(kwargs.keys())
for key in kwargs_keys:
    if key.startswith("experimental_"):
        attrs[key] = _get_experimental_kwarg_as_attr(key, kwargs[key])
        del kwargs[key]
    # Support for https://github.com/tensorflow/community/pull/113/files.
    elif key == "_implements" or key == "_reference":
        attrs[key] = _get_kwarg_as_str_attr(key, kwargs[key])
        del kwargs[key]
if kwargs:
    raise ValueError(f"Unknown keyword arguments: {kwargs.keys()}.")
exit(attrs)
