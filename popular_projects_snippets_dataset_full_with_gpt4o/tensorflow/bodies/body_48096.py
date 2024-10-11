# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
"""Prepares sample weight modes for the model.

  Args:
    training_endpoints: List of model _TrainingEndpoints.
    sample_weight_mode: sample weight mode user input passed from compile API.

  Raises:
    ValueError: In case of invalid `sample_weight_mode` input.
  """

if isinstance(sample_weight_mode, collections.abc.Mapping):
    generic_utils.check_for_unexpected_keys(
        'sample_weight_mode', sample_weight_mode,
        [e.output_name for e in training_endpoints])

    for end_point in training_endpoints:
        if not end_point.should_skip_target_weights():
            if end_point.output_name not in sample_weight_mode:
                raise ValueError('Output ' + end_point.output_name +
                                 'missing from `_sample_weight_modes` dictionary')
            else:
                end_point.sample_weight_mode = sample_weight_mode.get(
                    end_point.output_name)
elif isinstance(sample_weight_mode, (list, tuple)):
    if len(sample_weight_mode) != len(training_endpoints):
        raise ValueError('When passing a list as sample_weight_mode, '
                         'it should have one entry per model output. '
                         'The model has ' + str(len(training_endpoints)) +
                         ' outputs, but you passed ' +
                         str(len(sample_weight_mode)) + '_sample_weight_modes.')
    for mode, endpoint in zip(sample_weight_mode, training_endpoints):
        if not endpoint.should_skip_target_weights():
            endpoint.sample_weight_mode = mode
else:
    for endpoint in training_endpoints:
        if not endpoint.should_skip_target_weights():
            endpoint.sample_weight_mode = sample_weight_mode
