# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
"""Returns intermediate representation (usually a `Tensor`).

    Uses `inputs` to create an intermediate representation (usually a `Tensor`)
    that other feature columns can use.

    Example usage of `inputs`:
    Let's say a Feature column depends on raw feature ('raw') and another
    `_FeatureColumn` (input_fc). To access corresponding `Tensor`s, inputs will
    be used as follows:

    ```python
    raw_tensor = inputs.get('raw')
    fc_tensor = inputs.get(input_fc)
    ```

    Args:
      inputs: A `_LazyBuilder` object to access inputs.

    Returns:
      Transformed feature `Tensor`.
    """
pass
