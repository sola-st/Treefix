# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
"""Creates a regularization loss `Tensor` for variable `v`."""
with backend.name_scope(name + '/Regularizer'):
    regularization = regularizer(v)
exit(regularization)
