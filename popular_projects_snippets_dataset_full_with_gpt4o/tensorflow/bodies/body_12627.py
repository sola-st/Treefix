# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/batch_ops_test.py
"""Tests illegally feeding tensors with different dim0 sizes."""
if context.executing_eagerly():
    exit()
with self.cached_session() as sess:
    inp0 = array_ops.placeholder(dtype=dtypes.int32, shape=[1])
    inp1 = array_ops.placeholder(dtype=dtypes.int32, shape=[2])
    batched, index, _ = batch_ops.batch(
        [inp0, inp1], num_batch_threads=1, max_batch_size=2,
        batch_timeout_micros=0, grad_timeout_micros=0, batching_queue="")
    with self.assertRaises(Exception) as raised:
        _ = sess.run([batched, index], feed_dict={inp0: [0], inp1: [1, 2]})
    self.assertGreater(
        raised.exception.message.find("must have equal 0th-dimension size"),
        0)
