# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function.py
"""Sets `attrs` as attributes of self._c_func.

    Requires that self._c_func is not None.

    Args:
      attrs: a dictionary from attribute name to attribute proto value
    """
for name, attr_value in attrs.items():
    serialized = attr_value.SerializeToString()
    # TODO(skyewm): this creates and deletes a new TF_Status for every attr.
    # It might be worth creating a convenient way to re-use the same status.
    with self._c_func.get() as func:
        c_api.TF_FunctionSetAttrValueProto(func, compat.as_str(name),
                                           serialized)
