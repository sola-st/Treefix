# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/legacy_tf_layers/base.py
previous_losses_length = len(self._losses)
previous_callable_losses_length = len(self._callable_losses)
super(Layer, self).add_loss(losses, inputs=inputs)
if not context.executing_eagerly():
    # TODO(fchollet): deprecate collection below.
    new_losses = self._losses[previous_losses_length:]
    new_callable_losses = self._callable_losses[
        previous_callable_losses_length:]
    for regularizer in new_callable_losses:
        loss_tensor = regularizer()
        if loss_tensor is not None:
            new_losses.append(loss_tensor)
    _add_elements_to_collection(
        new_losses,
        ops.GraphKeys.REGULARIZATION_LOSSES)
