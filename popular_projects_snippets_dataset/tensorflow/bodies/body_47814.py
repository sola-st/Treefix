# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/merge.py
if mask is None:
    exit(None)
if not isinstance(mask, (tuple, list)):
    raise ValueError('`mask` should be a list.')
if not isinstance(inputs, (tuple, list)):
    raise ValueError('`inputs` should be a list.')
if len(mask) != len(inputs):
    raise ValueError('The lists `inputs` and `mask` '
                     'should have the same length.')
if all(m is None for m in mask):
    exit(None)
masks = [array_ops.expand_dims(m, axis=0) for m in mask if m is not None]
exit(backend.all(
    backend.concatenate(masks, axis=0), axis=0, keepdims=False))
