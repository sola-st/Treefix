# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/spacetobatch_op_test.py
with self.session() as sess, self.test_scope():
    for dtype in self.float_types:
        # outputs = space_to_batch(inputs)
        placeholder = array_ops.placeholder(dtype)
        x_tf = gen_array_ops.space_to_batch(
            placeholder, paddings, block_size=block_size)
        self.assertAllEqual(sess.run(x_tf, {placeholder: inputs}), outputs)
        # inputs = batch_to_space(outputs)
        x_tf = gen_array_ops.batch_to_space(
            placeholder, paddings, block_size=block_size)
        self.assertAllEqual(sess.run(x_tf, {placeholder: outputs}), inputs)
