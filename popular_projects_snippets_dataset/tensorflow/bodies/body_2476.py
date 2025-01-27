# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python_api/xla_literal.py
"""Converts a Numpy array to a XLA literal."""
type_record = types.MAP_DTYPE_TO_RECORD[str(ndarray.dtype)]
literal = xla_data_pb2.LiteralProto()
literal.shape.CopyFrom(xla_shape.CreateShapeFromNumpy(ndarray).message)

if ndarray.ndim == 0:
    getattr(literal, type_record.literal_field_name).append(
        ndarray.astype(type_record.literal_field_type).item())
else:
    # Ndarrays with boolean dtypes need special type conversion with protobufs
    if ndarray.dtype in {_np.bool_, _np.dtype('bool')}:
        for element in _np.nditer(ndarray):
            getattr(literal, type_record.literal_field_name).append(
                type_record.literal_field_type(element))
    else:
        ndarray_flat = ndarray.ravel(order='A')
        getattr(literal, type_record.literal_field_name).extend(ndarray_flat)
exit(literal)
