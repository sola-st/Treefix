# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Logs a weight as a TensorBoard image."""
w_img = array_ops.squeeze(weight)
shape = backend.int_shape(w_img)
if len(shape) == 1:  # Bias case
    w_img = array_ops.reshape(w_img, [1, shape[0], 1, 1])
elif len(shape) == 2:  # Dense layer kernel case
    if shape[0] > shape[1]:
        w_img = array_ops.transpose(w_img)
        shape = backend.int_shape(w_img)
    w_img = array_ops.reshape(w_img, [1, shape[0], shape[1], 1])
elif len(shape) == 3:  # ConvNet case
    if backend.image_data_format() == 'channels_last':
        # Switch to channels_first to display every kernel as a separate
        # image.
        w_img = array_ops.transpose(w_img, perm=[2, 0, 1])
        shape = backend.int_shape(w_img)
    w_img = array_ops.reshape(w_img, [shape[0], shape[1], shape[2], 1])

shape = backend.int_shape(w_img)
# Not possible to handle 3D convnets etc.
if len(shape) == 4 and shape[-1] in [1, 3, 4]:
    summary_ops_v2.image(weight_name, w_img, step=epoch)
