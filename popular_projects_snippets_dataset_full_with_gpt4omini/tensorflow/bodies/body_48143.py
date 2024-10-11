# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Test the model on a single batch of samples.

    Args:
        x: Input data. It could be:
          - A Numpy array (or array-like), or a list of arrays
            (in case the model has multiple inputs).
          - A TensorFlow tensor, or a list of tensors
            (in case the model has multiple inputs).
          - A dict mapping input names to the corresponding array/tensors,
            if the model has named inputs.
          - A `tf.data` dataset.
        y: Target data. Like the input data `x`,
          it could be either Numpy array(s) or TensorFlow tensor(s).
          It should be consistent with `x` (you cannot have Numpy inputs and
          tensor targets, or inversely). If `x` is a dataset `y` should
          not be specified (since targets will be obtained from the iterator).
        sample_weight: Optional array of the same length as x, containing
            weights to apply to the model's loss for each sample.
            In the case of temporal data, you can pass a 2D array
            with shape (samples, sequence_length),
            to apply a different weight to every timestep of every sample.
            In this case you should make sure to specify
            sample_weight_mode="temporal" in compile(). This argument is not
            supported when `x` is a dataset.
        reset_metrics: If `True`, the metrics returned will be only for this
          batch. If `False`, the metrics will be statefully accumulated across
          batches.

    Returns:
        Scalar test loss (if the model has a single output and no metrics)
        or list of scalars (if the model has multiple outputs
        and/or metrics). The attribute `model.metrics_names` will give you
        the display labels for the scalar outputs.

    Raises:
        ValueError: In case of invalid user-provided arguments.
    """
self._assert_compile_was_called()
self._check_call_args('test_on_batch')

if (self._distribution_strategy and
    distribution_strategy_context.in_cross_replica_context()):
    raise NotImplementedError('`test_on_batch` is not supported for models '
                              'distributed with tf.distribute.Strategy.')
# Validate and standardize user data.
x, y, sample_weights = self._standardize_user_data(
    x, y, sample_weight=sample_weight, extract_tensors_from_dataset=True)

# If `self._distribution_strategy` is True, then we are in a replica context
# at this point.
if self.run_eagerly or self._distribution_strategy:
    output_dict = training_eager_v1.test_on_batch(
        self,
        x,
        y,
        sample_weights=sample_weights,
        output_loss_metrics=self._output_loss_metrics)
    outputs = (output_dict['total_loss'] + output_dict['output_losses']
               + output_dict['metrics'])
    outputs = [_non_none_constant_value(v) for v in outputs]  # pylint: disable=protected-access
else:
    x = training_utils_v1.ModelInputs(x).as_list()
    inputs = x + list(y or []) + list(sample_weights or [])

    self._update_sample_weight_modes(sample_weights=sample_weights)
    self._make_test_function()
    outputs = self.test_function(inputs)  # pylint: disable=not-callable

if reset_metrics:
    self.reset_metrics()

if len(outputs) == 1:
    exit(outputs[0])
exit(outputs)
