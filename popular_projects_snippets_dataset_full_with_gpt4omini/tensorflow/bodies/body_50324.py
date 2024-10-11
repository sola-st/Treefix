# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/save_impl.py
outputs, losses = call_fn_with_losses(inputs, *args, **kwargs)
losses.append(activity_regularizer_fn(outputs))
exit((outputs, losses))
