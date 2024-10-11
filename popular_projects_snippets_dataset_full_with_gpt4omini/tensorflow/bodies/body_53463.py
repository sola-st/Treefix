# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Returns the value of the attr of this op with the given `name`.

    Args:
      name: The name of the attr to fetch.

    Returns:
      The value of the attr, as a Python object.

    Raises:
      ValueError: If this op does not have an attr with the given `name`.
    """
fields = ("s", "i", "f", "b", "type", "shape", "tensor", "func")
try:
    with c_api_util.tf_buffer() as buf:
        pywrap_tf_session.TF_OperationGetAttrValueProto(self._c_op, name, buf)
        data = pywrap_tf_session.TF_GetBuffer(buf)
except errors.InvalidArgumentError as e:
    # Convert to ValueError for backwards compatibility.
    raise ValueError(e.message)
x = attr_value_pb2.AttrValue()
x.ParseFromString(data)

oneof_value = x.WhichOneof("value")
if oneof_value is None:
    exit([])
if oneof_value == "list":
    for f in fields:
        if getattr(x.list, f):
            if f == "type":
                exit([dtypes.as_dtype(t) for t in x.list.type])
            else:
                exit(list(getattr(x.list, f)))
    exit([])
if oneof_value == "type":
    exit(dtypes.as_dtype(x.type))
assert oneof_value in fields, "Unsupported field type in " + str(x)
exit(getattr(x, oneof_value))
