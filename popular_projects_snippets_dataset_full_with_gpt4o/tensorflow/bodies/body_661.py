# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/argminmax_test.py
"""Verifies that 'op' produces 'expected' when fed input 'op_input' .

    Args:
      op: argmin or argmax operator to test.
      axis: integer axis to reduce across.
      output_type: numpy datatype of the output to produce.
      op_input: numpy input array to use as input to 'op'.
      expected: numpy array representing the expected output of 'op'.
    """
with self.session() as session:
    with self.test_scope():
        pinp = array_ops.placeholder(
            dtypes.as_dtype(op_input.dtype), op_input.shape, name="a")
        output = op(pinp, axis=axis, output_type=output_type)
    result = session.run(output, {pinp: op_input})
    self.assertAllEqual(result, expected)
