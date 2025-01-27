# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/shape_ops_test.py
if context.executing_eagerly():
    exit()
with self.session():
    signal_shape = (2, 128)
    signal = array_ops.ones(signal_shape)
    frame_length = 33
    frame_step = 9
    frames = shape_ops.frame(signal, frame_length, frame_step)
    error = test.compute_gradient_error(
        signal, signal_shape, frames, frames.shape.as_list())
    self.assertLess(error, 2e-5)
