# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/utils.py
"""Creates fn that adds the losses returned by call_fn & returns the outputs.

  Args:
    layer: A Keras layer object
    call_fn: tf.function that takes layer inputs (and possibly a training arg),
      and returns a tuple of (outputs, list of losses).
    default_training_value: Default value of the training kwarg. If `None`, the
      default is `K.learning_phase()`.
    return_method: Whether to return a method bound to the layer.

  Returns:
    function that calls call_fn and returns the outputs. Losses returned by
    call_fn are added to the layer losses.
  """
expects_training_arg = layer_uses_training_bool(layer)
if hasattr(call_fn, 'original_layer_call'):  # call_fn is a LayerCall object
    original_call = call_fn.original_layer_call
    # In Python 3, callable objects are not compatible with inspect.getargspec
    call_fn = call_fn.__call__
else:
    original_call = call_fn
fn, arg_spec = maybe_add_training_arg(
    original_call, call_fn, expects_training_arg, default_training_value)

def return_outputs_and_add_losses(*args, **kwargs):
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

decorated = tf_decorator.make_decorator(
    target=call_fn,
    decorator_func=return_outputs_and_add_losses,
    decorator_argspec=arg_spec)

if return_method:
    exit(types.MethodType(decorated, layer))
else:
    exit(decorated)
