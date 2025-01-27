# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_with_v1_optimizers_test.py
checkpoint_directory = self.get_temp_dir()

root = trackable_utils.Checkpoint()
root.var = trackable_utils.add_variable(
    root, name="var", initializer=0.)
optimizer = adam.AdamOptimizer(0.1)
if context.executing_eagerly():
    optimizer.minimize(root.var.read_value)
else:
    train_op = optimizer.minimize(root.var)
    # Note that `optimizer` has not been added as a dependency of
    # `root`. Create a one-off grouping so that slot variables for `root.var`
    # get initialized too.
    self.evaluate(trackable_utils.gather_initializers(
        trackable_utils.Checkpoint(root=root, optimizer=optimizer)))
    self.evaluate(train_op)
self.evaluate(state_ops.assign(root.var, 12.))
no_slots_path = root.save(os.path.join(checkpoint_directory, "no_slots"))
root.optimizer = optimizer
self.evaluate(state_ops.assign(root.var, 13.))
self.evaluate(state_ops.assign(optimizer.get_slot(name="m", var=root.var),
                               14.))
slots_path = root.save(os.path.join(checkpoint_directory, "with_slots"))
new_root = trackable_utils.Checkpoint()
# Load the slot-containing checkpoint (deferred), then immediately overwrite
# the non-slot variable (also deferred).
slot_status = new_root.restore(slots_path)
no_slot_status = new_root.restore(no_slots_path)
with self.assertRaises(AssertionError):
    no_slot_status.assert_consumed()
new_root.var = trackable_utils.add_variable(
    new_root, name="var", shape=[])
no_slot_status.assert_consumed()
no_slot_status.run_restore_ops()
self.assertEqual(12., self.evaluate(new_root.var))
new_root.optimizer = adam.AdamOptimizer(0.1)
slot_status.assert_existing_objects_matched()
with self.assertRaisesRegex(AssertionError, "beta1_power"):
    slot_status.assert_consumed()
self.assertEqual(12., self.evaluate(new_root.var))
if context.executing_eagerly():
    # Slot variables are only created with restoring initializers when
    # executing eagerly.
    self.assertEqual(14., self.evaluate(
        new_root.optimizer.get_slot(name="m", var=new_root.var)))
else:
    self.assertIs(new_root.optimizer.get_slot(name="m", var=new_root.var),
                  None)
if context.executing_eagerly():
    new_root.optimizer.minimize(new_root.var.read_value)
else:
    train_op = new_root.optimizer.minimize(new_root.var)
    # The slot variable now exists; restore() didn't create it, but we should
    # now have a restore op for it.
    slot_status.run_restore_ops()
    self.assertEqual(14., self.evaluate(
        new_root.optimizer.get_slot(name="m", var=new_root.var)))
    self.evaluate(train_op)
slot_status.assert_consumed()
