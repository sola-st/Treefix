# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Test the model on a single batch of samples.

    Args:
        x: Input data. It could be:
          - A Numpy array (or array-like), or a list of arrays (in case the
              model has multiple inputs).
          - A TensorFlow tensor, or a list of tensors (in case the model has
              multiple inputs).
          - A dict mapping input names to the corresponding array/tensors, if
              the model has named inputs.
        y: Target data. Like the input data `x`, it could be either Numpy
          array(s) or TensorFlow tensor(s). It should be consistent with `x`
          (you cannot have Numpy inputs and tensor targets, or inversely).
        sample_weight: Optional array of the same length as x, containing
          weights to apply to the model's loss for each sample. In the case of
          temporal data, you can pass a 2D array with shape (samples,
          sequence_length), to apply a different weight to every timestep of
          every sample.
        reset_metrics: If `True`, the metrics returned will be only for this
          batch. If `False`, the metrics will be statefully accumulated across
          batches.
        return_dict: If `True`, loss and metric results are returned as a dict,
          with each key being the name of the metric. If `False`, they are
          returned as a list.

    Returns:
        Scalar test loss (if the model has a single output and no metrics)
        or list of scalars (if the model has multiple outputs
        and/or metrics). The attribute `model.metrics_names` will give you
        the display labels for the scalar outputs.

    Raises:
        RuntimeError: If `model.test_on_batch` is wrapped in `tf.function`.
        ValueError: In case of invalid user-provided arguments.
    """
self._assert_compile_was_called()
self._check_call_args('test_on_batch')
_disallow_inside_tf_function('test_on_batch')
with self.distribute_strategy.scope():
    iterator = data_adapter.single_batch_iterator(self.distribute_strategy, x,
                                                  y, sample_weight)
    self.test_function = self.make_test_function()
    logs = self.test_function(iterator)

if reset_metrics:
    self.reset_metrics()
logs = tf_utils.sync_to_numpy_or_python_type(logs)
if return_dict:
    exit(logs)
else:
    exit(flatten_metrics_in_order(logs, self.metrics_names))
