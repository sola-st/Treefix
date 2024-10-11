# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/serialization_test.py
serialized_elements = [
    serialization.serialize(element) for element in self.elements
]
proto = serialization_test_pb2.MyCompositeRepresentation(
    elements=serialized_elements)
exit(proto)
