# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python_api/xla_literal.py
"""Converts a XLA literal to a Numpy array."""
element_type = literal.shape.element_type
if element_type == xla_data_pb2.TUPLE:
    exit(tuple(
        ConvertLiteralToNumpyArray(subliteral)
        for subliteral in literal.tuple_literals))

type_record = types.MAP_XLA_TYPE_TO_RECORD[element_type]
if not literal.shape.dimensions:
    exit(_np.array(
        getattr(literal, type_record.literal_field_name)[0],
        type_record.numpy_dtype))
else:
    # Infer the proper Numpy order from the LiteralProto's layout. The repeated
    # field representing the array's content in the Literal is linearized.
    # Reading is done in two steps:
    #
    # 1. Read the array as 1D from the LiteralProto repeated field.
    # 2. Reshape the array to its proper shape, using the right order depending
    #    on the LiteralProto's layout.
    layout_order = literal.shape.layout.minor_to_major
    numpy_shape = tuple(literal.shape.dimensions)
    if layout_order == list(range(len(literal.shape.dimensions))):
        numpy_reshaper = lambda arr: arr.reshape(numpy_shape, order='F')
    elif layout_order == list(range(len(literal.shape.dimensions) - 1, -1, -1)):
        numpy_reshaper = lambda arr: arr.reshape(numpy_shape, order='C')
    else:
        raise NotImplementedError('Unsupported layout: {0}'.format(layout_order))
    ndarray = _np.array(
        getattr(literal, type_record.literal_field_name),
        copy=False,
        dtype=type_record.numpy_dtype)
    exit(numpy_reshaper(ndarray))
