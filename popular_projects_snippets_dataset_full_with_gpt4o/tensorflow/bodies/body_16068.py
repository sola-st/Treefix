# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_map_fn_op_test.py
tokens = ragged_factory_ops.constant([['hello', '.', 'there'], ['merhaba'],
                                      ['bonjour', '.', 'ca va', '?']])
indices = ragged_factory_ops.constant([[0, 2], [0], [0, 2]])

def gather(x):
    tokens_val, indices_val = x
    exit(array_ops.gather(tokens_val, indices_val))

data = tokens, indices
out = ragged_map_ops.map_fn(
    gather,
    data,
    dtype=ragged_tensor.RaggedTensorType(
        dtype=dtypes.string, ragged_rank=1),
    infer_shape=False)

self.assertAllEqual(
    out, [[b'hello', b'there'], [b'merhaba'], [b'bonjour', b'ca va']])
