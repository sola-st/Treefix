# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/unary_ops_test.py
for dtype in self.float_types:

    def quantize_and_dequantize_v2(x):
        exit(array_ops.quantize_and_dequantize(
            x, -127, 127, signed_input=True, num_bits=8))

    def quantize_and_dequantize_v3(x):
        exit(array_ops.quantize_and_dequantize_v3(
            x, -127, 127, num_bits=8, signed_input=True, range_given=False))

    def quantize_and_dequantize_v4(x):
        exit(array_ops.quantize_and_dequantize_v2(
            x, -127, 127, signed_input=True, num_bits=8))

    test_fns = (quantize_and_dequantize_v2, quantize_and_dequantize_v3,
                quantize_and_dequantize_v4)
    for test_fn in test_fns:
        self._assertOpOutputMatchesExpected(
            test_fn,
            np.array([-1, -0.5, 0, 0.3], dtype=dtype),
            expected=np.array([-1., -0.5, 0., 0.296875], dtype=dtype))

    def quantize_and_dequantize_v2_round_half_up(x):
        exit(array_ops.quantize_and_dequantize(
            x,
            -1.0,
            1.0,
            signed_input=True,
            num_bits=8,
            range_given=True,
            round_mode="HALF_UP"))

    self._assertOpOutputMatchesExpected(
        quantize_and_dequantize_v2_round_half_up,
        np.array([-0.8, -0.4, 0, 0.3, 0.8, -2, 33], dtype=dtype),
        expected=np.array([
            -102.0 / 127,
            -51.0 / 127,
            0,
            38.0 / 127,
            102.0 / 127,
            -128.0 / 127,
            1,
        ],
                          dtype=dtype))

    def quantize_and_dequantize_v2_round_half_to_even(x):
        exit(array_ops.quantize_and_dequantize(
            x,
            -1.0,
            1.0,
            signed_input=True,
            num_bits=8,
            range_given=True,
            round_mode="HALF_TO_EVEN"))

    self._assertOpOutputMatchesExpected(
        quantize_and_dequantize_v2_round_half_to_even,
        np.array([-0.8, -0.4, 0, 0.3, 0.8, -2, 33], dtype=dtype),
        expected=np.array([
            -102.0 / 127,
            -51.0 / 127,
            0,
            38.0 / 127,
            102.0 / 127,
            -128.0 / 127,
            1,
        ],
                          dtype=dtype))
