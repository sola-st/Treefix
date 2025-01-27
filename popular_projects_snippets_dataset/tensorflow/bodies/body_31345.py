# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_test.py
cell = Plus1RNNCell()
if context.executing_eagerly():
    inputs = [constant_op.constant(np.ones((3, 4)))]
else:
    inputs = [array_ops.placeholder(dtypes.float32, shape=(3, 4))]
with self.assertRaisesRegex(ValueError, "must be a vector"):
    rnn.dynamic_rnn(
        cell,
        array_ops.stack(inputs),
        dtype=dtypes.float32,
        sequence_length=[[4]])
