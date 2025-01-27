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
    for grad, param in zip(unreduced_gradients, parameters):
        param.assign_sub(0.01 * grad)
final_kernels = self.device.unpack(layer.kernel)
self.assertNotAllClose(final_kernels[0], final_kernels[1])
final_bias = self.device.unpack(layer.bias)
self.assertAllClose(1. - 0.01 * 2. * (1. - .5 - math_ops.range(5.)),
                    final_bias[0])
self.assertAllClose(1. - 0.01 * 2. * (1. + .5 - math_ops.range(5.)),
                    final_bias[1])
self.assertIn(self.device.components[0], final_kernels[0].backing_device)
self.assertIn(self.device.components[1], final_kernels[1].backing_device)
