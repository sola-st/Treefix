# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Returns predictions for a single batch of samples.

    Args:
        x: Input data. It could be:
          - A Numpy array (or array-like), or a list of arrays
            (in case the model has multiple inputs).
          - A TensorFlow tensor, or a list of tensors
            (in case the model has multiple inputs).
          - A `tf.data` dataset.

    Returns:
        Numpy array(s) of predictions.

    Raises:
        ValueError: In case of mismatch between given number of inputs and
          expectations of the model.
    """
self._check_call_args('predict_on_batch')

if (self._distribution_strategy and
    distribution_strategy_context.in_cross_replica_context()):
    raise NotImplementedError(
        '`predict_on_batch` is not supported for models distributed with'
        ' tf.distribute.Strategy.')
# Validate and standardize user data.
inputs, _, _ = self._standardize_user_data(
    x, extract_tensors_from_dataset=True)
# If `self._distribution_strategy` is True, then we are in a replica context
# at this point.
if self.run_eagerly or self._distribution_strategy:
    inputs = training_utils_v1.cast_if_floating_dtype(inputs)
    if isinstance(inputs, collections.abc.Sequence):
        # Unwrap lists with only one input, as we do when training on batch
        if len(inputs) == 1:
            inputs = inputs[0]

    exit(self(inputs))  # pylint: disable=not-callable

self._make_predict_function()
outputs = self.predict_function(inputs)

if len(outputs) == 1:
    exit(outputs[0])
exit(outputs)
