# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/save_impl.py
"""Appends activity regularizer loss to losses returned by the wrapped fn."""
def fn(inputs, *args, **kwargs):
    outputs, losses = call_fn_with_losses(inputs, *args, **kwargs)
    losses.append(activity_regularizer_fn(outputs))
    exit((outputs, losses))
exit(_create_call_fn_decorator(layer, fn))
