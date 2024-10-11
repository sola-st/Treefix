# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/einsum_op_test.py
"""Verifies that unary 'op' produces 'expected' when fed input 'inp'."""
with self.session() as session:
    with self.test_scope():
        pinp = array_ops.placeholder(
            dtypes.as_dtype(inp.dtype), inp.shape, name='a')
        output = op(pinp)
    result = session.run(output, {pinp: inp})
    self.assertEqual(output.dtype, expected.dtype)
    self.assertAllCloseAccordingToType(
        expected, result, rtol=1e-3, atol=1e-5, bfloat16_rtol=0.03)
