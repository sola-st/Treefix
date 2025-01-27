# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2.py
"""Check the incoming output shapes against the output shapes stored."""
# The incoming output shape should have the same structure with the existing
# output shapes.
nest.assert_same_structure(self._output_shapes, incoming_output_shapes)

for (path, _), old_output_shape, incoming_output_shape in zip(
    nest.flatten_with_joined_string_paths(self._feature_config),
    self._output_shapes, incoming_output_shapes):
    # First check if both shapes are not None.
    if old_output_shape and incoming_output_shape:
        # We skip the check when the incoming output shape is rank 1 or 2 and
        # rank of the old output shape is larger. This can happen for
        # (sequence) ragged tensor, we push the check down to the enqueue op.
        if (len(incoming_output_shape) == 1 or len(incoming_output_shape)
            == 2) and len(old_output_shape) > len(incoming_output_shape):
            continue
        if len(old_output_shape) != len(
            incoming_output_shape) or not self._is_tensor_shape_match(
                old_output_shape, incoming_output_shape):
            raise ValueError(
                f"Inconsistent shape founded for input feature {path}, "
                f"Output shape is set to be {old_output_shape}, "
                f"But got incoming output shape {incoming_output_shape}")
