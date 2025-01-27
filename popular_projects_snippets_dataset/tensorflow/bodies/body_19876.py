# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2.py
"""Get output shapes from the flattened input shapes list."""
output_shapes = []
for input_shape, feature in zip(input_shapes,
                                nest.flatten(self._feature_config)):
    if input_shape.rank is None or input_shape.rank < 1:
        raise ValueError(
            "Received input tensor of shape {}. Rank must be 1 and above"
            .format(input_shape))
    # Update the input shape with the max sequence length. Only update when
    # 1. Input feature is 2D ragged or sparse tensor.
    # 2. Output shape is not set in the feature config and the max sequence
    #    length is set.
    if (len(input_shape) == 2 and input_shape[-1] != 1 and
        not feature.output_shape and feature.max_sequence_length > 0):
        input_shape_list = input_shape.as_list()
        input_shape_list.insert(
            len(input_shape_list) - 1, feature.max_sequence_length)
        input_shape = TensorShape(input_shape_list)
    if input_shape.rank == 1:
        output_shapes.append(input_shape)
    else:
        output_shapes.append(input_shape[:-1])
exit(output_shapes)
