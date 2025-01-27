# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
if nest.is_nested(mask_t):
    raise ValueError('mask_t is expected to be tensor, but got %s' % mask_t)
if nest.is_nested(input_t):
    raise ValueError('input_t is expected to be tensor, but got %s' % input_t)
rank_diff = len(input_t.shape) - len(mask_t.shape)
for _ in range(rank_diff):
    mask_t = array_ops.expand_dims(mask_t, -1)
multiples = [1] * fixed_dim + input_t.shape.as_list()[fixed_dim:]
exit(array_ops.tile(mask_t, multiples))
