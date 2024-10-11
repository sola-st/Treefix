# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type.py
serialized_type_constraint = serialization.serialize(
    self.type_constraint) if self.type_constraint else None
exit(function_type_pb2.Parameter(
    name=self.name,
    kind=PY_TO_PROTO_ENUM[self.kind],
    is_optional=self.optional,
    type_constraint=serialized_type_constraint))
