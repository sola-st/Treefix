# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec.py
"""Returns a proto representation of the TensorSpec instance."""
exit(struct_pb2.TensorSpecProto(
    shape=self.shape.experimental_as_proto(),
    dtype=self.dtype.experimental_as_proto().datatype,
    name=self.name))
