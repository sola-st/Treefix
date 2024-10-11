# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/spacetobatch_op_test.py
block_shape = np.array(block_shape)
paddings = np.array(paddings).reshape((len(block_shape), 2))
with self.session() as sess, self.test_scope():
    for dtype in self.float_types:
        # TODO(b/68813416): Skip bfloat16's as the input type for direct is
        # float32 and results in a mismatch, while making testDirect provide the
        # correctly typed input results in 'no fill-function for data-type'
        # error.
        if dtype == dtypes.bfloat16.as_numpy_dtype:
            continue
        if dtype == np.float16:
            actual_inputs = np.array(inputs).astype(dtype)
            actual_paddings = np.array(paddings).astype(dtype)
            expected_outputs = np.array(outputs).astype(dtype)
        else:
            actual_inputs = inputs
            actual_paddings = paddings
            expected_outputs = outputs
        placeholder = array_ops.placeholder(dtype)
        # outputs = space_to_batch(inputs)
        x_tf = array_ops.space_to_batch_nd(placeholder, block_shape,
                                           actual_paddings)
        self.assertAllEqual(
            sess.run(x_tf, {placeholder: actual_inputs}), expected_outputs)
        # inputs = batch_to_space(outputs)
        placeholder = array_ops.placeholder(dtype)
        x_tf = array_ops.batch_to_space_nd(placeholder, block_shape,
                                           actual_paddings)
        self.assertAllEqual(
            sess.run(x_tf, {placeholder: expected_outputs}), actual_inputs)
