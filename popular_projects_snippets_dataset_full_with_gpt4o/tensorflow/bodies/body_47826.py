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
# Make a list of masks while making sure
# the dimensionality of each mask
# is the same as the corresponding input.
masks = []
for input_i, mask_i in zip(inputs, mask):
    if mask_i is None:
        # Input is unmasked. Append all 1s to masks,
        masks.append(array_ops.ones_like(input_i, dtype='bool'))
    elif backend.ndim(mask_i) < backend.ndim(input_i):
        # Mask is smaller than the input, expand it
        masks.append(array_ops.expand_dims(mask_i, axis=-1))
    else:
        masks.append(mask_i)
concatenated = backend.concatenate(masks, axis=self.axis)
exit(backend.all(concatenated, axis=-1, keepdims=False))
