# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/reconstruction_ops_test.py
# TODO(rjryan): Eager gradient tests.
if context.executing_eagerly():
    exit()
signal = array_ops.zeros((2, 10, 10))
frame_hop = 10
reconstruction = reconstruction_ops.overlap_and_add(signal, frame_hop)

# Multiply the first batch-item's reconstruction by zeros. This will block
# gradient from flowing into the first batch item from the loss. Multiply
# the second batch item by the integers from 0 to 99. Since there is zero
# overlap, the gradient for this batch item will be 0-99 shaped as (10,
# 10).
reconstruction *= array_ops.stack(
    [array_ops.zeros((100,)),
     math_ops.cast(math_ops.range(100), dtypes.float32)])
loss = math_ops.reduce_sum(reconstruction)

# Verify that only the second batch item receives gradient.
gradient = self.evaluate(gradients_impl.gradients([loss], [signal])[0])
expected_gradient = np.stack([
    np.zeros((10, 10)),
    np.reshape(np.arange(100).astype(np.float32), (10, 10))])
self.assertAllEqual(expected_gradient, gradient)
