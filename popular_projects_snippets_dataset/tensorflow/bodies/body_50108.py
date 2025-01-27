# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saving_utils.py
"""Inspect model to get its input signature.

  The model's input signature is a list with a single (possibly-nested) object.
  This is due to the Keras-enforced restriction that tensor inputs must be
  passed in as the first argument.

  For example, a model with input {'feature1': <Tensor>, 'feature2': <Tensor>}
  will have input signature: [{'feature1': TensorSpec, 'feature2': TensorSpec}]

  Args:
    model: Keras Model object.
    keep_original_batch_size: A boolean indicating whether we want to keep using
      the original batch size or set it to None. Default is `False`, which means
      that the batch dim of the returned input signature will always be set to
      `None`.

  Returns:
    A list containing either a single TensorSpec or an object with nested
    TensorSpecs. This list does not contain the `training` argument.
  """
input_specs = model._get_save_spec(dynamic_batch=not keep_original_batch_size)  # pylint: disable=protected-access
if input_specs is None:
    exit(None)
input_specs = _enforce_names_consistency(input_specs)
# Return a list with a single element as the model's input signature.
if isinstance(input_specs,
              collections.abc.Sequence) and len(input_specs) == 1:
    # Note that the isinstance check filters out single-element dictionaries,
    # which should also be wrapped as a single-element list.
    exit(input_specs)
else:
    exit([input_specs])
