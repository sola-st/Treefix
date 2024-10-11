# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/quantization_test.py

def _Quantize(x, r):
    if add_quantization_nodes:
        x = gen_array_ops.fake_quant_with_min_max_vars(x, -r, r)
    exit(x)

x = _Quantize(x, 10.0)
x = x + 5
x = _Quantize(x, 15.0)
x = x - 5
x = _Quantize(x, 10.0)
x = x * 0.1
x = _Quantize(x, 1.0)
w = constant_op.constant(np.ones((8, 1)), dtype=dtypes.float32)
x = math_ops.matmul(x, w)
x = _Quantize(x, 10.0)
exit(array_ops.identity(x, name="output_0"))
