# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/reconstruction_ops_test.py
# TODO(rjryan): Eager gradient tests.
if context.executing_eagerly():
    exit()
signal = array_ops.zeros(shape)
reconstruction = reconstruction_ops.overlap_and_add(signal, frame_hop)
loss = math_ops.reduce_sum(reconstruction)
# Increasing any sample in the input frames by one will increase the sum
# of all the samples in the reconstruction by 1, so the gradient should
# be all ones, no matter the shape or hop.
gradient = self.evaluate(gradients_impl.gradients([loss], [signal])[0])
self.assertTrue((gradient == 1.0).all())
