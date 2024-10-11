# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/quantize_model.py
"""Validates the representative dataset, based on the signature keys.

  Representative dataset can be provided in two different forms: a single
  instance of `RepresentativeDataset` or a map of signature key to the
  corresponding `RepresentativeDataset`. These have a relationship with
  `signature_keys`.

  This function validates the following conditions:
  * If `len(signature_keys) > 1`, then `representative_dataset` should be a
    mapping where the keys exactly match the elements in `signature_keys`.
  * If `len(signature_keys) == 1`, then both a mapping and a single instance of
    `RepresentativeDataset` are allowed.
  * This function also assumes `len(signature_keys) > 0`.

  Args:
    representative_dataset: A `RepresentativeDataset` or a map of string to
      `RepresentativeDataset` to be validated.
    signature_keys: A collection of strings that contains the signature keys,
      each identifying a `SignatureDef`.

  Raises:
    ValueError: Iff `representative_dataset` does not satisfy the conditions
      above.
  """
if isinstance(representative_dataset, collections.abc.Mapping):
    if set(signature_keys) != set(representative_dataset.keys()):
        raise ValueError(
            'The signature keys and the keys of representative dataset map '
            f'do not match. Signature keys: {set(signature_keys)}, '
            f'representative dataset map: {set(representative_dataset.keys())}.'
        )
else:
    if len(signature_keys) > 1:
        raise ValueError(
            'Representative dataset is not a mapping '
            f'(got: {type(representative_dataset)}), '
            'but there is more than one signature key provided. '
            'Please provide a map of {signature_key -> dataset} '
            'with more than one signature key.'
        )
