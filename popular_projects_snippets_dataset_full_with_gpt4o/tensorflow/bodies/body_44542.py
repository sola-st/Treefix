# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
"""Ensures that the condition can be used in a TF control flow."""
extra_hint = 'to check for None, use `is not None`'
cond = ops.convert_to_tensor_v2(cond)

if cond.dtype != dtypes.bool:
    raise ValueError(
        'condition of {} expected to be `tf.bool` scalar, got {}'
        '; to use as boolean Tensor, use `tf.cast`'
        '; {}'.format(tag, cond, extra_hint))

if cond.shape is None or cond.shape.ndims is None:
    # TODO(mdan): Consider a explicit size check, if not too slow.
    cond = array_ops.reshape(cond, ())

elif cond.shape.ndims > 0:
    known_dims = [d for d in cond.shape.as_list() if d is not None]
    if np.prod(known_dims) > 1:
        raise ValueError(
            'condition of {} expected to be `tf.bool` scalar, got {}'
            '; {}'.format(tag, cond, extra_hint))
    else:
        cond = array_ops.reshape(cond, ())

exit(cond)
