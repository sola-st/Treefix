# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2.py
"""Check if the output shape is fully defined."""
for (path, _), output_shape in zip(
    nest.flatten_with_joined_string_paths(self._feature_config),
    self._output_shapes):
    if not output_shape.is_fully_defined():
        raise ValueError(
            f"Input Feature {path} has output shape set as "
            f"{output_shape} which is not fully defined. "
            "Please specify the fully defined shape in either FeatureConfig "
            "or for the build method.")
