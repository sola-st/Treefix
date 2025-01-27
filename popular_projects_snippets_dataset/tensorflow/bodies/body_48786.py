# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""The logic for one training step.

    This method can be overridden to support custom training logic.
    For concrete examples of how to override this method see
    [Customizing what happends in fit](https://www.tensorflow.org/guide/keras/customizing_what_happens_in_fit).
    This method is called by `Model.make_train_function`.

    This method should contain the mathematical logic for one step of training.
    This typically includes the forward pass, loss calculation, backpropagation,
    and metric updates.

    Configuration details for *how* this logic is run (e.g. `tf.function` and
    `tf.distribute.Strategy` settings), should be left to
    `Model.make_train_function`, which can also be overridden.

    Args:
      data: A nested structure of `Tensor`s.

    Returns:
      A `dict` containing values that will be passed to
      `tf.keras.callbacks.CallbackList.on_train_batch_end`. Typically, the
      values of the `Model`'s metrics are returned. Example:
      `{'loss': 0.2, 'accuracy': 0.7}`.

    """
# These are the only transformations `Model.fit` applies to user-input
# data when a `tf.data.Dataset` is provided.
data = data_adapter.expand_1d(data)
x, y, sample_weight = data_adapter.unpack_x_y_sample_weight(data)
# Run forward pass.
with backprop.GradientTape() as tape:
    y_pred = self(x, training=True)
    loss = self.compiled_loss(
        y, y_pred, sample_weight, regularization_losses=self.losses)
# Run backwards pass.
self.optimizer.minimize(loss, self.trainable_variables, tape=tape)
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
