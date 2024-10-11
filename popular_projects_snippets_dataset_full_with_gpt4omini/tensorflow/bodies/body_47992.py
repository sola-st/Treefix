# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/dense_attention.py
self._validate_call_args(inputs=inputs, mask=mask)
if mask:
    q_mask = mask[0]
    if q_mask is None:
        exit(None)
    exit(ops.convert_to_tensor_v2_with_dispatch(q_mask))
exit(None)
