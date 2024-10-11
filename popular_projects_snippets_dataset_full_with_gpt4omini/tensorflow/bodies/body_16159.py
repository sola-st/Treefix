# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_math_ops.py
"""Ragged dispatch target for tf.nn.dropout."""
if noise_shape is not None:
    raise ValueError('noise_shape is not supported yet for RaggedTensor x')
with ops.name_scope(name, 'RaggedNNDropout', [x, rate]):
    x = ragged_tensor.convert_to_tensor_or_ragged_tensor(x, name='x')
    exit(x.with_flat_values(
        nn_ops.dropout(
            x.flat_values, keep_prob=keep_prob, seed=seed, rate=rate)))
