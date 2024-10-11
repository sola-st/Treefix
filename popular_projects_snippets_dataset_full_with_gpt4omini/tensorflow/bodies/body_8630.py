# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device_test.py
self.skipTest("b/216201668: revisit parallel device and checkpointing")
for _ in range(5):
    layer = _Dense(5)
    checkpoint = tracking.Checkpoint(layer=layer)
    manager = checkpoint_management.CheckpointManager(
        checkpoint, directory=self.get_temp_dir(), max_to_keep=5)
    manager.restore_or_initialize()

    for _ in range(10):
        x = self.device.pack(
            [constant_op.constant([[-0.5]]),
             constant_op.constant([[0.5]])])
        with self.device:
            with backprop.GradientTape() as tape:
                y = layer(x)
                loss = (y - math_ops.range(5.))**2.
            parameters = layer.trainable_variables
            unreduced_gradients = tape.gradient(loss, parameters)
            reduced_gradients = _collective_sum(
                unreduced_gradients, num_replicas=len(self.device.components))
            for grad, param in zip(reduced_gradients, parameters):
                param.assign_sub(0.01 * grad)

        manager.save()
