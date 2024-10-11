# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/losses.py
num_classes = math_ops.cast(array_ops.shape(y_true)[-1], y_pred.dtype)
exit(y_true * (1.0 - label_smoothing) + (label_smoothing / num_classes))
