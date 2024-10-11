# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device_test.py
self.skipTest("b/216201668: revisit parallel device and checkpointing.")

prefix = os.path.join(self.get_temp_dir(), "ckpt")
different_values = self.device.pack(
    [constant_op.constant(-1.),
     constant_op.constant(3.)])
with self.device:
    v = variables.Variable(different_values)
    checkpoint = tracking.Checkpoint(v=v)
save_path = checkpoint.save(prefix)
with self.device:
    v.assign(constant_op.constant(0.))
checkpoint.restore(save_path).assert_consumed()
with self.device:
    outputs = self.device.unpack(v)
self.assertAllClose([-1., 3.], outputs)

with self.device:
    restore_on_create = tracking.Checkpoint()
    restore_on_create.restore(save_path)
    restore_on_create.v = variables.Variable(0.)
    outputs = self.device.unpack(restore_on_create.v)
self.assertAllClose([-1., 3.], outputs)

# Changing the number of devices / restoring into a single-device copy is OK
single_device = tracking.Checkpoint(v=variables.Variable(0.))
status = single_device.restore(save_path)
status.assert_existing_objects_matched()
self.assertAllClose(-1., single_device.v)
with self.assertRaisesRegex(AssertionError, "parallel_component_1"):
    # There are parts of the variable that aren't restored into a
    # single-device copy.
    status.assert_consumed()
