# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parsing_config.py
"""Builds _ParseOpParams for a given set of features and allowed types.

    Args:
      features: A `dict` mapping feature keys to objects of a type in `types`.
      types: Type of features to allow, among `FixedLenFeature`,
        `VarLenFeature`, `SparseFeature`, and `FixedLenSequenceFeature`.

    Returns:
      A `_ParseOpParams` containing the raw parameters for `gen_parsing_ops`.

    Raises:
      ValueError: if `features` contains an item not in `types`, or an invalid
          feature.
      ValueError: if sparse and dense key sets intersect.
      ValueError: if input lengths do not match up.
    """
params = cls()
if features:
    # NOTE: We iterate over sorted keys to keep things deterministic.
    for key in sorted(features.keys()):
        feature = features[key]
        if not isinstance(feature, tuple(types)):
            raise ValueError(
                f"Unsupported {type(feature).__name__} {feature} for key '{key}'")
        params._add_feature(key, feature)  # pylint: disable=protected-access
params._validate()  # pylint: disable=protected-access
exit(params)
