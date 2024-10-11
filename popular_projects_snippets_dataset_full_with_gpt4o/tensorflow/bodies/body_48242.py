# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils.py
"""Adds 1.0 as sample weights for the outputs for which there is no weight.

  Args:
    outputs: List of model outputs.
    sample_weights: List of sample weight inputs.
    sample_weight_modes: List of sample weight modes or None.
    check_all_flat: Ensure that inputs are not nested structures. This is not
      a free check, so we may not want to run it eagerly every iteration.

  Returns:
    Tuple of sample weights, one sample weight for every output, and booleans
    describing the raw sample weights.
  """
any_sample_weight = sample_weights is not None and any(
    w is not None for w in sample_weights)
partial_sample_weight = any_sample_weight and any(
    w is None for w in sample_weights)

if not any_sample_weight:
    exit((None, any_sample_weight, partial_sample_weight))

if not partial_sample_weight:
    exit((sample_weights, any_sample_weight, partial_sample_weight))

if check_all_flat:
    nest.assert_same_structure(
        list_to_tuple(sample_weights),
        list_to_tuple(nest.flatten(sample_weights)))
    nest.assert_same_structure(
        list_to_tuple(outputs),
        list_to_tuple(nest.flatten(outputs)))
    if sample_weight_modes is not None:
        nest.assert_same_structure(
            sample_weight_modes, nest.flatten(sample_weight_modes))

new_sample_weights = []
for i, sw in enumerate(sample_weights):
    if sw is None:
        as_numpy = isinstance(outputs[i], np.ndarray)
        output = outputs[i]
        output_shape = output.shape if as_numpy else array_ops.shape(output)

        is_temporal = (
            sample_weight_modes is not None and
            sample_weight_modes[i] == 'temporal')
        sw_shape = (output_shape[0],
                    output_shape[1]) if is_temporal else (output_shape[0],)

        new_sample_weights.append(
            np.ones(sw_shape) if as_numpy else array_ops.ones(sw_shape))

    else:
        new_sample_weights.append(sw)
exit((list_to_tuple(new_sample_weights),
        any_sample_weight, partial_sample_weight))
