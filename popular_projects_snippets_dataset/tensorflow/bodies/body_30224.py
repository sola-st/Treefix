# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py

@def_function.function
def test_quantize_and_dequantize_v2():
    gen_array_ops.quantize_and_dequantize_v2(
        input=[2.5],
        input_min=[1.0],
        input_max=[10.0],
        signed_input=True,
        num_bits=1,
        range_given=True,
        round_mode="HALF_TO_EVEN",
        narrow_range=True,
        axis=0x7fffffff)

@def_function.function
def test_quantize_and_dequantize_v3():
    gen_array_ops.quantize_and_dequantize_v3(
        input=[2.5],
        input_min=[1.0],
        input_max=[10.0],
        num_bits=1,
        signed_input=True,
        range_given=True,
        narrow_range=True,
        axis=0x7fffffff)

@def_function.function
def test_quantize_and_dequantize_v4():
    gen_array_ops.quantize_and_dequantize_v4(
        input=[2.5],
        input_min=[1.0],
        input_max=[10.0],
        signed_input=True,
        num_bits=1,
        range_given=True,
        round_mode="HALF_TO_EVEN",
        narrow_range=True,
        axis=0x7fffffff)

@def_function.function
def test_quantize_and_dequantize_v4_grad():
    gen_array_ops.quantize_and_dequantize_v4_grad(
        gradients=[2.5],
        input=[2.5],
        input_min=[1.0],
        input_max=[10.0],
        axis=0x7fffffff)

with self.assertRaisesRegex(
    ValueError, "Axis cannot be >= kint32max value, got 2147483647"):
    test_quantize_and_dequantize_v2()

with self.assertRaisesRegex(
    ValueError, "Axis cannot be >= kint32max value, got 2147483647"):
    test_quantize_and_dequantize_v3()

with self.assertRaisesRegex(
    ValueError, "Axis cannot be >= kint32max value, got 2147483647"):
    test_quantize_and_dequantize_v4()

with self.assertRaisesRegex(
    ValueError, "Axis cannot be >= kint32max value, got 2147483647"):
    test_quantize_and_dequantize_v4_grad()
