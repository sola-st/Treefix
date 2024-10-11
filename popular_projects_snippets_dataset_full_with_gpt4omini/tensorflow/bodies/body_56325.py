# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/dtypes.py
"""Returns a proto representation of the Dtype instance."""
exit(types_pb2.SerializedDType(datatype=self._type_enum))
