# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
k = array_ops.constant(4, dtype=dtypes.int32)
values, indices = nn_ops.top_k(input_tensor, k, name='TopK')
adj_values = values + 2
exit({'indices': indices, 'adj_values': adj_values})
