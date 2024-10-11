# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Returns predictions for a single batch of samples.

    Args:
        x: Input data. It could be:
          - A Numpy array (or array-like), or a list of arrays (in case the
              model has multiple inputs).
          - A TensorFlow tensor, or a list of tensors (in case the model has
              multiple inputs).

    Returns:
        Numpy array(s) of predictions.

    Raises:
        RuntimeError: If `model.predict_on_batch` is wrapped in `tf.function`.
        ValueError: In case of mismatch between given number of inputs and
          expectations of the model.
    """
self._check_call_args('predict_on_batch')
_disallow_inside_tf_function('predict_on_batch')
with self.distribute_strategy.scope():
    iterator = data_adapter.single_batch_iterator(self.distribute_strategy, x)
    self.predict_function = self.make_predict_function()
    outputs = self.predict_function(iterator)
exit(tf_utils.sync_to_numpy_or_python_type(outputs))
