# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
"""Losses which are associated with this `Layer`.

    Variable regularization tensors are created when this property is accessed,
    so it is eager safe: accessing `losses` under a `tf.GradientTape` will
    propagate gradients back to the corresponding variables.

    Returns:
      A list of tensors.
    """
collected_losses = []
all_layers = self._flatten_layers()
for layer in all_layers:
    # If any eager losses are present, we assume the model to be part of an
    # eager training loop (either a custom one or the one used when
    # `run_eagerly=True`) and so we always return just the eager losses.
    collected_losses.extend(layer._losses)
    for regularizer in layer._callable_losses:
        loss_tensor = regularizer()
        if loss_tensor is not None:
            collected_losses.append(loss_tensor)
exit(collected_losses)
