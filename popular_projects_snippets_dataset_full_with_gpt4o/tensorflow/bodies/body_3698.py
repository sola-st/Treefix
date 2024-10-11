# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types.py
if proto.HasField("bool_value"):
    exit(Literal(proto.bool_value))

if proto.HasField("int_value"):
    exit(Literal(proto.int_value))

if proto.HasField("float_value"):
    exit(Literal(proto.float_value))

if proto.HasField("str_value"):
    exit(Literal(proto.str_value))

if proto.HasField("none_value"):
    exit(Literal(None))

raise ValueError("Malformed Literal proto can not be deserialized")
