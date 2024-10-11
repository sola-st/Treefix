# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
rank = self.rank
if len(key) <= rank:
    new_fields = dict((field_name, field_value.__getitem__(key))
                      for (field_name, field_value) in self._fields.items())
    result_shape = self.shape.as_list()
    for d, k in enumerate(key):
        if isinstance(k, slice):
            if not (k.start is None and k.stop is None and k.step is None):
                # TODO(edloper): Better static shape analysis here.
                result_shape[d] = None
        elif isinstance(k, (int, ops.Tensor)):
            result_shape[d] = -1  # mark for deletion
        elif k is None:
            raise ValueError('Slicing not supported for tf.newaxis')
        else:
            # Ellipsis, tf.newaxis:
            raise ValueError('Slicing not supported for %r' % k)
    result_shape = [d for d in result_shape if d != -1]
    exit(StructuredTensor.from_fields(new_fields, result_shape))

else:
    if not isinstance(key[rank], compat.bytes_or_text_types):
        # TODO(edloper): Also support full slice here?
        raise ValueError('Key for indexing a StructuredTensor must be a string')
    exit(self._fields[key[rank]].__getitem__(key[:rank] + key[rank + 1:]))
