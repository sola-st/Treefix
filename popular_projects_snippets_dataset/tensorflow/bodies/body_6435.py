# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/vars_test.py
aggregation = [
    variable_scope.VariableAggregation.NONE,
    variable_scope.VariableAggregation.ONLY_FIRST_REPLICA,
    variable_scope.VariableAggregation.SUM,
    variable_scope.VariableAggregation.MEAN
]
for agg in aggregation:
    v_normal_restore = variables_lib.Variable(1.0)
    v_normal_save = variables_lib.Variable(3.0)
    with strategy.scope():
        v_on_write = variables_lib.Variable(2.0, aggregation=agg)

        # Save ONWRITE Restore ONWRITE
        # Save
        ckpt = trackable_utils.Checkpoint(var=v_on_write)
        manager = ckpt_manager.CheckpointManager(
            ckpt, "/tmp/ckpt_" + str(uuid.uuid4()), max_to_keep=None)
        manager.save()
        # Restore
        ckpt.restore(manager.latest_checkpoint)
        self.assertEqual(2.0, self.evaluate(v_on_write._values[0]))
        self.assertEqual(2.0, self.evaluate(v_on_write.read_value()))

        # Save Mirrored Restore Normal
        # We've already saved Mirrored, so we only need to restore normal
        ckpt_normal = trackable_utils.Checkpoint(var=v_normal_restore)
        ckpt_normal.restore(manager.latest_checkpoint)
        self.assertEqual(2.0, self.evaluate(v_on_write._values[0]))
        self.assertEqual(2.0, self.evaluate(v_normal_restore.read_value()))

        # Save Normal Restore Mirrored
        # Save
        ckpt = trackable_utils.Checkpoint(var=v_normal_save)
        manager_2 = ckpt_manager.CheckpointManager(
            ckpt, "/tmp/ckptckpt_" + str(uuid.uuid4()), max_to_keep=None)
        manager_2.save()
        # Restore
        ckpt_on_write = trackable_utils.Checkpoint(var=v_on_write)
        ckpt_on_write.restore(manager_2.latest_checkpoint)
        self.assertEqual(3.0, self.evaluate(v_on_write._values[0]))
        self.assertEqual(3.0, self.evaluate(v_on_write.read_value()))
