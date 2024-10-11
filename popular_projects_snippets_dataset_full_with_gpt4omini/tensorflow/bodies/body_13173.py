# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parsing_ops.py
"""Returns a copy of features with adjusted FixedLenSequenceFeature shapes."""
if features:
    modified_features = dict(features)  # Create a copy to modify
    for key, feature in features.items():
        if isinstance(feature, FixedLenSequenceFeature):
            if not feature.allow_missing:
                raise ValueError("Unsupported: FixedLenSequenceFeature requires "
                                 "allow_missing to be True.")
            modified_features[key] = FixedLenSequenceFeature(
                [None] + list(feature.shape),
                feature.dtype,
                feature.allow_missing,
                feature.default_value)
    exit(modified_features)
else:
    exit(features)
