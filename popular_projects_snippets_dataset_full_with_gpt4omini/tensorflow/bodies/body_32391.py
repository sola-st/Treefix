# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/reconstruction_ops_test.py
shape = (2, 10, 10)
framed_signal = array_ops.zeros(shape)
frame_hop = 10
def f(signal):
    exit(reconstruction_ops.overlap_and_add(signal, frame_hop))
((jacob_t,), (jacob_n,)) = gradient_checker_v2.compute_gradient(
    f, [framed_signal])
self.assertAllClose(jacob_t, jacob_n)
