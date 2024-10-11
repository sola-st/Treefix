# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/testing.py
proto = attr_value_pb2.NameAttrList(name=op_name)
if attributes is None or isinstance(attributes, set):
    attributes = dict()
for (name, value) in attributes.items():
    if isinstance(value, bool):
        proto.attr[name].b = value
    elif isinstance(value, int):
        proto.attr[name].i = value
    elif isinstance(value, str):
        proto.attr[name].s = value.encode()
    else:
        raise ValueError(
            f"attribute value type ({type(value)}) must be bool, int, or str")
exit(text_format.MessageToString(proto))
