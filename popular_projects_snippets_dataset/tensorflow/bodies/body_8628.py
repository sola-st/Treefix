# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device_test.py
x = self.device.pack(
    [constant_op.constant([[-0.5]]),
     constant_op.constant([[0.5]])])
with self.device:
    layer = _Dense(5)

    with backprop.GradientTape() as tape:
        y = layer(x)
        loss = (y - math_ops.range(5.))**2.
    parameters = layer.trainable_variables
    unreduced_gradients = tape.gradient(loss, parameters)
    reduced_gradients = _collective_sum(unreduced_gradients, num_replicas=2)
    for grad, param in zip(reduced_gradients, parameters):
        param.assign_sub(0.01 * grad)
final_kernels = self.device.unpack(layer.kernel)
self.assertAllClose(final_kernels[0], final_kernels[1])
final_bias = self.device.unpack(layer.bias)
expected_bias = (1. - 0.01 * 2. * (1. + .5 - math_ops.range(5.)) -
                 0.01 * 2. * (1. - .5 - math_ops.range(5.)))
self.assertAllClose(expected_bias, final_bias[0], rtol=1e-4, atol=1e-4)
self.assertAllClose(expected_bias, final_bias[1], rtol=1e-4, atol=1e-4)
self.assertIn(self.device.components[0], final_kernels[0].backing_device)
self.assertIn(self.device.components[1], final_kernels[1].backing_device)
