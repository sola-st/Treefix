# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/quantization_test.py
if add_quantization_nodes:
    x = gen_array_ops.fake_quant_with_min_max_vars(x, -r, r)
exit(x)
