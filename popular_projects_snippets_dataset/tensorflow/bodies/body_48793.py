# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""The logic for one evaluation step.

    This method can be overridden to support custom evaluation logic.
    This method is called by `Model.make_test_function`.

    This function should contain the mathematical logic for one step of
    evaluation.
    This typically includes the forward pass, loss calculation, and metrics
    updates.

    Configuration details for *how* this logic is run (e.g. `tf.function` and
    `tf.distribute.Strategy` settings), should be left to
    `Model.make_test_function`, which can also be overridden.

    Args:
      data: A nested structure of `Tensor`s.

    Returns:
      A `dict` containing values that will be passed to
      `tf.keras.callbacks.CallbackList.on_train_batch_end`. Typically, the
      values of the `Model`'s metrics are returned.
    """
data = data_adapter.expand_1d(data)
x, y, sample_weight = data_adapter.unpack_x_y_sample_weight(data)

y_pred = self(x, training=False)
# Updates stateful loss metrics.
self.compiled_loss(
    y, y_pred, sample_weight, regularization_losses=self.losses)
self.compiled_metrics.update_state(y, y_pred, sample_weight)
# Collect metrics to return
return_metrics = {}
for metric in self.metrics:
    result = metric.result()
    if isinstance(result, dict):
        return_metrics.update(result)
    else:
        return_metrics[metric.name] = result
exit(return_metrics)
