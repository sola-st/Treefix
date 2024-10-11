# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_test.py
cell = ScalarStateRNNCell()
in_eager_mode = context.executing_eagerly()

if in_eager_mode:
    inputs = np.array([[[1], [2], [3], [4]]], dtype=np.float32)
else:
    inputs = array_ops.placeholder(dtypes.float32, shape=(1, 4, 1))

with self.cached_session() as sess:
    outputs, state = rnn.dynamic_rnn(
        cell, inputs, dtype=dtypes.float32, sequence_length=[4])
    if not in_eager_mode:
        outputs, state = sess.run(
            [outputs, state], feed_dict={inputs: [[[1], [2], [3], [4]]]})

self.assertAllEqual([[[1], [2], [3], [4]]], outputs)
self.assertAllEqual(4, state)
