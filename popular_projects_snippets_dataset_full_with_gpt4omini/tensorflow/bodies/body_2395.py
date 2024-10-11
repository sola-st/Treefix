# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/reduce_ops_test.py
"""Tests reduce sum on a list of input arrays.

    For each array in test_inputs, check that performing reduce sum on the array
    produces a value that is close to the expected result.

    Args:
      expected_result: the expected result.
      dtype: the data type of the reduce sum operation.
      test_inputs: a list of input arrays for the reduce sum operation.
      rtol: the relative error.
      atol: the absolute error.
    """

for test_input in test_inputs:
    with self.session() as sess:
        with self.test_scope():
            a = array_ops.placeholder(dtype)
            index = array_ops.placeholder(dtypes.int32)
            out = math_ops.reduce_sum(a, index)
        result = sess.run(out, {
            a: np.array(test_input, dtype=dtype),
            index: [0]
        })
        # Compare the results using float32 type.
        self.assertAllClose(
            np.float32(result),
            np.float32(expected_result),
            rtol=rtol,
            atol=atol)
