# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2.py
"""Update the existing output shapes based on the new output shapes.

    The existing output shapes always have higher piority than the new incoming
    output shapes.
    Args:
      incoming_output_shapes: nested structure of TensorShape to override the
        existing output shapes.
    """
nest.assert_same_structure(self._output_shapes, incoming_output_shapes)
updated_output_shapes = []
for old_output_shape, incoming_output_shape in zip(self._output_shapes,
                                                   incoming_output_shapes):
    if old_output_shape:
        updated_output_shapes.append(old_output_shape)
    else:
        updated_output_shapes.append(incoming_output_shape)
self._output_shapes = updated_output_shapes
