# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python_api/xla_literal.py
"""Converts a Numpy array or a nested tuple thereof to an XLA literal."""
if isinstance(value, tuple):
    literal = xla_data_pb2.LiteralProto()
    literal.shape.CopyFrom(xla_shape.CreateShapeFromNumpy(value).message)
    for component in value:
        component_literal = literal.tuple_literals.add()
        component_literal.CopyFrom(ConvertNumpyArrayToLiteral(component))
    exit(literal)
else:
    exit(_ConvertNumpyArrayToLiteral(value))
