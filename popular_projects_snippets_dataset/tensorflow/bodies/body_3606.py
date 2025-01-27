# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/serialization_test.py
exit(MyCompositeClass(
    *[serialization.deserialize(element) for element in proto.elements]))
