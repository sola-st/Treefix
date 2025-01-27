# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
"""Prepare feed values to the model execution function.

  Args:
    model: Model to prepare feed values for.
    inputs: List or dict of model inputs.
    targets: Optional list of model targets.
    sample_weights: Optional list of sample weight arrays.
    mode: One of ModeKeys.TRAIN/ModeKeys.TEST/ModeKeys.PREDICT.

  Returns:
    Feed values for the model in the given mode.
  """
strategy = model._distribution_strategy
inputs, targets, sample_weights = _get_input_from_iterator(inputs, model)
if backend.is_tpu_strategy(strategy):
    if sample_weights is not None:
        raise ValueError('TPUStrategy does not support sample weights.')

  # When the inputs are dict, then we want to flatten it in the same order as
  # the input layers, such that the data are fed into the input layers in the
  # correct order.
if isinstance(inputs, dict):
    inputs = [inputs[key] for key in model._feed_input_names]
if is_distributing_by_cloning(model):
    inputs = flatten_per_replica_values(strategy, inputs)
    targets = flatten_per_replica_values(strategy, targets)
    # Expand 1-dimensional inputs.
    # TODO(b/124535720): Remove once this standarize data logic is shared with
    # main flow.
    inputs, targets = nest.map_structure(
        training_utils_v1.standardize_single_array, (inputs, targets))
else:
    inputs = training_utils_v1.ModelInputs(inputs).as_list()

if mode == ModeKeys.PREDICT:
    sample_weights = []
    targets = []
elif sample_weights is not None and is_distributing_by_cloning(model):
    if context.executing_eagerly() and not model._compile_distribution:
        raise NotImplementedError('`sample_weight` is not supported when using '
                                  'tf.distribute.Strategy in eager mode and '
                                  'cloning=True.')
    sample_weights = flatten_per_replica_values(strategy, sample_weights)

ins = [inputs, targets, sample_weights]
exit(tuple(ins))
