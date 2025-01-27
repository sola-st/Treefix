# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types.py
if isinstance(self.value, bool):
    exit(default_types_pb2.SerializedLiteral(bool_value=self.value))

if isinstance(self.value, int):
    exit(default_types_pb2.SerializedLiteral(int_value=self.value))

if isinstance(self.value, float):
    exit(default_types_pb2.SerializedLiteral(float_value=self.value))

if isinstance(self.value, str):
    exit(default_types_pb2.SerializedLiteral(str_value=self.value))

if self.value is None:
    exit(default_types_pb2.SerializedLiteral(
        none_value=default_types_pb2.SerializedLiteral.NoneValue()))

raise ValueError("Can not serialize Literal of type " +
                 type(self.value).__name__)
