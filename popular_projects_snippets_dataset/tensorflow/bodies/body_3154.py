# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
q_input = array_ops.fake_quant_with_min_max_args(
    input_tensor, min=-0.1, max=0.2, num_bits=8, narrow_range=False
)
adj_values = q_input + 2
exit({'adj_values_1': adj_values, 'adj_values_2': adj_values})
