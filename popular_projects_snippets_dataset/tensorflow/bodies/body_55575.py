# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library.py
"""Encodes a Python value as an `AttrValue` proto message.

  Args:
    value: The value to convert.
    attr_type: The value type (string) -- see the AttrValue proto definition for
      valid strings.
    arg_name: Argument name (for error messages).

  Returns:
    An AttrValue proto message that encodes `value`.
  """
attr_value = attr_value_pb2.AttrValue()

if attr_type.startswith("list("):
    if not _IsListValue(value):
        raise TypeError(f"Expected list for attr {arg_name}, obtained "
                        f"{type(value).__name__} instead.")

if attr_type == "string":
    attr_value.s = _MakeStr(value, arg_name)
elif attr_type == "list(string)":
    attr_value.list.s.extend([_MakeStr(x, arg_name) for x in value])
elif attr_type == "int":
    attr_value.i = _MakeInt(value, arg_name)
elif attr_type == "list(int)":
    attr_value.list.i.extend([_MakeInt(x, arg_name) for x in value])
elif attr_type == "float":
    attr_value.f = _MakeFloat(value, arg_name)
elif attr_type == "list(float)":
    attr_value.list.f.extend([_MakeFloat(x, arg_name) for x in value])
elif attr_type == "bool":
    attr_value.b = _MakeBool(value, arg_name)
elif attr_type == "list(bool)":
    attr_value.list.b.extend([_MakeBool(x, arg_name) for x in value])
elif attr_type == "type":
    attr_value.type = _MakeType(value, arg_name)
elif attr_type == "list(type)":
    attr_value.list.type.extend([_MakeType(x, arg_name) for x in value])
elif attr_type == "shape":
    attr_value.shape.CopyFrom(_MakeShape(value, arg_name))
elif attr_type == "list(shape)":
    attr_value.list.shape.extend([_MakeShape(x, arg_name) for x in value])
elif attr_type == "tensor":
    attr_value.tensor.CopyFrom(_MakeTensor(value, arg_name))
elif attr_type == "list(tensor)":
    attr_value.list.tensor.extend([_MakeTensor(x, arg_name) for x in value])
elif attr_type == "func":
    attr_value.func.CopyFrom(_MakeFunc(value, arg_name))
elif attr_type == "list(func)":
    attr_value.list.func.extend([_MakeFunc(x, arg_name) for x in value])
else:
    raise TypeError(f"Unrecognized Attr type {attr_type} for {arg_name}.")
exit(attr_value)
