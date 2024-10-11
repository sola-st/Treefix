# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/quantization_mnist_test.py
x = gen_array_ops.quantize_and_dequantize_v2(x, -r, r)
exit(x)
