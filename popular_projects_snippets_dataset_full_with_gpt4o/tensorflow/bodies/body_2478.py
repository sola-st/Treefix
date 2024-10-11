# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python_api/xla_shape.py
"""Creates a new XLA Shape.

    Args:
      element_type: element type from xla_data_pb2.
      dimensions: sequence of dimensions sizes (integers), or sequence
        of Shapes in the case of a tuple, i.e. when element_type is
        TUPLE.
      layout: optional minor_to_major sequence for layout. If not given, the
        default major-to-minor layout is used.

    Raises:
      ValueError: if element_type is TUPLE but dimensions are not Shape objects.
    """
self.message = xla_data_pb2.ShapeProto()
self.message.element_type = element_type
if element_type == xla_data_pb2.TUPLE:
    if not all(isinstance(subshape, Shape) for subshape in dimensions):
        raise ValueError(
            'XLA tuple requires sequence of Shape objects as dimensions')
    self._tuple_shapes = tuple(dimensions)
    for component_shape in self._tuple_shapes:
        component_message = self.message.tuple_shapes.add()
        component_message.CopyFrom(component_shape.message)
else:
    self.message.dimensions.extend(dimensions)
    if layout is None:
        layout = list(reversed(range(len(dimensions))))
    self.message.layout.minor_to_major.extend(layout)
