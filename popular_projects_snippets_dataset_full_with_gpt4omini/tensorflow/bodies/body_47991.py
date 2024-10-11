# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/dense_attention.py
self._validate_call_args(inputs=inputs, mask=mask)
q = inputs[0]
v = inputs[1]
k = inputs[2] if len(inputs) > 2 else v
q_mask = mask[0] if mask else None
v_mask = mask[1] if mask else None
scores = self._calculate_scores(query=q, key=k)
if v_mask is not None:
    # Mask of shape [batch_size, 1, Tv].
    v_mask = array_ops.expand_dims(v_mask, axis=-2)
if self.causal:
    # Creates a lower triangular mask, so position i cannot attend to
    # positions j>i. This prevents the flow of information from the future
    # into the past.
    scores_shape = array_ops.shape(scores)
    # causal_mask_shape = [1, Tq, Tv].
    causal_mask_shape = array_ops.concat(
        [array_ops.ones_like(scores_shape[:-2]), scores_shape[-2:]],
        axis=0)
    causal_mask = _lower_triangular_mask(causal_mask_shape)
else:
    causal_mask = None
scores_mask = _merge_masks(v_mask, causal_mask)
result, attention_scores = self._apply_scores(
    scores=scores, value=v, scores_mask=scores_mask, training=training)
if q_mask is not None:
    # Mask of shape [batch_size, Tq, 1].
    q_mask = array_ops.expand_dims(q_mask, axis=-1)
    result *= math_ops.cast(q_mask, dtype=result.dtype)
if return_attention_scores:
    exit((result, attention_scores))
exit(result)
