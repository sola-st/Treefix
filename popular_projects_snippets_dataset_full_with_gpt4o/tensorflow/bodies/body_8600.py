# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device_test.py
previous = config.get_synchronous_execution()
try:
    context._reset_context()
    config.set_synchronous_execution(False)
    self.setUp()
    # Note that ops on the parallel device currently don't execute
    # asynchronously. The test is just that we don't get deadlocks.
    x = self.device.pack(
        [constant_op.constant(-1.5),
         constant_op.constant(3.5)])
    with self.device:
        reduced = _collective_sum(x, num_replicas=2)
        outputs = self.device.unpack(reduced)
    self.assertAllClose([2., 2.], outputs)
    self.assertIn(self.device.components[0], outputs[0].backing_device)
    self.assertIn(self.device.components[1], outputs[1].backing_device)
finally:
    context._reset_context()
    config.set_synchronous_execution(previous)
