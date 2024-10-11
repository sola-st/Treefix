# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/shape_ops_test.py
if context.executing_eagerly():
    exit()
# Show that frame works even when the dimensions of its input are
# not known at graph creation time.
input_signal = np.vstack([np.arange(4), np.arange(4) + 10,
                          np.arange(4) + 20])
frame_length = 2
frame_step = 2

signal_placeholder = array_ops.placeholder_with_default(
    input_signal, shape=(None, None))
result = self.evaluate(
    shape_ops.frame(signal_placeholder, frame_length, frame_step))
self.assertAllEqual([[[0, 1], [2, 3]],
                     [[10, 11], [12, 13]],
                     [[20, 21], [22, 23]]], result)
