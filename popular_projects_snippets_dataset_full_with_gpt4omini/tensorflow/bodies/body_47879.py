# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
super(Permute, self).__init__(**kwargs)
self.dims = tuple(dims)
if sorted(dims) != list(range(1, len(dims) + 1)):
    raise ValueError(
        'Invalid permutation `dims` for Permute Layer: %s. '
        'The set of indices in `dims` must be consecutive and start from 1.' %
        (dims,))
self.input_spec = InputSpec(ndim=len(self.dims) + 1)
