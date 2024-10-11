# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_math_ops_test.py
dense = rt.to_tensor()
result = math_ops.cumsum(dense, axis=axis, exclusive=exclusive,
                         reverse=reverse, name=name)
exit(ragged_tensor.RaggedTensor.from_tensor(
    result, lengths=rt.nested_row_lengths()))
