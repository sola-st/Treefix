# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec.py
"""Returns a proto representation of the BoundedTensorSpec instance."""
exit(struct_pb2.BoundedTensorSpecProto(
    shape=self.shape.experimental_as_proto(),
    dtype=self.dtype.experimental_as_proto().datatype,
    minimum=tensor_util.make_tensor_proto(self._minimum),
    maximum=tensor_util.make_tensor_proto(self._maximum),
    name=self.name))
