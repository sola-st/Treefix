# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types.py
exit(default_types_pb2.SerializedNamedTuple(
    type_name=self.type_name,
    attribute_names=list(self.attribute_names),
    attributes=self.attributes.experimental_as_proto()))
