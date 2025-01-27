# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
"""Restore unconditional losses from SavedModel."""
if hasattr(_get_keras_attr(layer), 'layer_regularization_losses'):
    losses = getattr(_get_keras_attr(layer), 'layer_regularization_losses', [])
else:
    # Some earlier SavedModels may not have layer_regularization_losses
    # serialized separately. Fall back to using the regularization_losses
    # list if it does not exist.
    losses = layer._serialized_attributes.get('regularization_losses', [])  # pylint: disable=protected-access
for loss in losses:
    layer.add_loss(loss)
