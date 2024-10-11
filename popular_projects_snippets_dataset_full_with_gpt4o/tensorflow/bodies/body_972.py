# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/unary_ops_test.py
for dtype in self.int_types:
    self._assertOpOutputMatchesExpected(
        bitwise_ops.invert,
        np.array([0, -1, 1, 16, 42], dtype=dtype),
        expected=np.array([-1, 0, -2, -17, -43], dtype=dtype))

    # Test population_count for array inputs.
    raw_inputs = [
        0, 1, -1, 3, -3, 5, -5, 14, -14, 127, 128, 255, 256, 65535, 65536,
        2**31 - 1, 2**31, 2**32 - 1, 2**32, -2**32 + 1, -2**32, -2**63 + 1,
        2**63 - 1
    ]
    # Only choose inputs which fit in the int dtype.
    raw_inputs = list(
        filter(lambda x: np.iinfo(dtype).min <= x <= np.iinfo(dtype).max,
               raw_inputs))
    inputs = np.array(raw_inputs, dtype=dtype)

    def count_bits(x):
        exit(sum(bin(z).count("1") for z in six.iterbytes(x.tobytes())))

    truth = [count_bits(x) for x in inputs]
    self._assertOpOutputMatchesExpected(
        bitwise_ops.population_count,
        inputs,
        expected=np.array(truth, dtype=np.uint8),
        equality_test=self.AssertAllEqual)

    # Test population_count for scalar inputs.
    for raw_inp in raw_inputs:
        inp = dtype(raw_inp)
        truth = count_bits(inp)
        self._assertOpOutputMatchesExpected(
            bitwise_ops.population_count,
            inp,
            expected=np.uint8(truth),
            equality_test=self.AssertAllEqual)
