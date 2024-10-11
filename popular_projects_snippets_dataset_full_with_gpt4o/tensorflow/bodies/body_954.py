# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/unary_ops_test.py
"""Verifies that 'op' produces 'expected' when fed input 'inp' .

    Args:
      op: operator to test
      inp: numpy input array to use as input to 'op'.
      expected: numpy array representing the expected output of 'op'.
      equality_test: either None, or a function that tests two numpy arrays for
        equality. If None, self.assertAllClose is used.
      rtol: relative tolerance for equality test.
      atol: absolute tolerance for equality test.
    """
with self.session() as session:
    with self.test_scope():
        pinp = array_ops.placeholder(
            dtypes.as_dtype(inp.dtype), inp.shape, name="a")
        output = op(pinp)
    result = session.run(output, {pinp: inp})
    if equality_test is None:
        self.assertEqual(output.dtype, expected.dtype)
        self.assertAllCloseAccordingToType(
            expected, result, rtol=rtol, atol=atol, bfloat16_rtol=0.03)
    else:
        equality_test(result, expected, rtol=rtol, atol=atol)
