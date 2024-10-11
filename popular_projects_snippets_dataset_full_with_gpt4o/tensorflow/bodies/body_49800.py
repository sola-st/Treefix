# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/constraints.py
w_shape = w.shape
if w_shape.rank is None or w_shape.rank != 4:
    raise ValueError(
        'The weight tensor must be of rank 4, but is of shape: %s' % w_shape)

height, width, channels, kernels = w_shape
w = backend.reshape(w, (height, width, channels * kernels))
# TODO(cpeter): Switch map_fn for a faster tf.vectorized_map once
# backend.switch is supported.
w = backend.map_fn(
    self._kernel_constraint,
    backend.stack(array_ops.unstack(w, axis=-1), axis=0))
exit(backend.reshape(backend.stack(array_ops.unstack(w, axis=0), axis=-1),
                       (height, width, channels, kernels)))
