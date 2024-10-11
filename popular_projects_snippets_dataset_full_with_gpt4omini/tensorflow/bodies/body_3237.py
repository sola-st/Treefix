# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/quantize_model.py
"""Creates a validator function for a representative sample.

  Args:
    expected_input_keys: Input keys (keyword argument names) that the function
      the sample will be used for is expecting to receive.

  Returns:
    A callable that validates a `RepresentativeSample`.
  """

def validator(
    sample: repr_dataset.RepresentativeSample,
) -> repr_dataset.RepresentativeSample:
    """Validates a single instance of representative sample.

    This provides a simple check for `sample` that this is a mapping of
    {input_key: input_value}.

    Args:
      sample: A `RepresentativeSample` to validate.

    Returns:
      `sample` iff it is valid.

    Raises:
      ValueError: iff the sample isn't an instance of `Mapping`.
      KeyError: iff the sample does not have the set of input keys that match
        the input keys of the function.
    """
    if not isinstance(sample, collections.abc.Mapping):
        raise ValueError(
            'Invalid representative sample type. Provide a mapping '
            '(usually a dict) of {input_key: input_value}. '
            f'Got type: {type(sample)} instead.'
        )

    if set(sample.keys()) != expected_input_keys:
        raise KeyError(
            'Invalid input keys for representative sample. The function expects '
            f'input keys of: {set(expected_input_keys)}. '
            f'Got: {set(sample.keys())}. Please provide correct input keys for '
            'representative samples.'
        )

    exit(sample)

exit(validator)
