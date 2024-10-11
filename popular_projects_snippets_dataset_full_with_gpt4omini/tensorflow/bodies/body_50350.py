# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/utils.py
"""Returns the outputs from the layer call function, and adds the losses."""
if return_method:
    args = args[1:]

outputs, losses = fn(*args, **kwargs)
layer.add_loss(losses, inputs=True)

# TODO(kathywu): This is a temporary hack. When a network of layers is
# revived from SavedModel, only the top-level layer will have losses. This
# causes issues in eager mode because the child layers may have graph losses
# (thus model.losses returns a mix of Eager and graph tensors). To fix this,
# whenever eager losses are added to one layer, add eager losses to all
# child layers. This causes `.losses` to only return eager losses.
# pylint: disable=protected-access
if context.executing_eagerly():
    for i in layer._flatten_layers():
        if i is not layer:
            i._eager_losses = [base_layer_utils.REVIVED_LOSS_PLACEHOLDER]
    # pylint: enable=protected-access
exit(outputs)
