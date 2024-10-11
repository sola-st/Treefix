# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/vars_test.py
aggregation = [variable_scope.VariableAggregation.SUM,
               variable_scope.VariableAggregation.MEAN]
for agg in aggregation:
    v_normal_restore = variables_lib.Variable(1.0)
    v_normal_save = variables_lib.Variable(2.0)

    with strategy.scope():
        v_on_read = variables_lib.Variable(
            1.0, synchronization=variable_scope.VariableSynchronization.ON_READ,
            aggregation=agg)

        @def_function.function
        def assign_fn():
            cluster_resolver = strategy.cluster_resolver
            replica_ctx = ds_context.get_replica_context()
            if ((cluster_resolver and cluster_resolver.task_type == "worker") or
                math_ops.equal(replica_ctx.replica_id_in_sync_group,
                               constant_op.constant(1))):
                v_on_read.assign(3.)  # pylint:disable=cell-var-from-loop
            else:
                v_on_read.assign(4.)  # pylint:disable=cell-var-from-loop

        strategy.run(assign_fn)

        # Save ONREAD, restore ONREAD
        # Saves v[0] + v[1] = 7 for SUM and 3.5 for MEAN.
        ckpt = trackable_utils.Checkpoint(var=v_on_read)
        manager = ckpt_manager.CheckpointManager(
            ckpt, "/tmp/ckpt_" + str(uuid.uuid4()), max_to_keep=None)
        manager.save()
        # Restores a value of 7/2 = 3.5 for SUM and 3.5 for MEAN.
        ckpt.restore(manager.latest_checkpoint)
        self.assertEqual(3.5, self.evaluate(v_on_read._values[0]))

        # Save ONREAD, restore normal
        ckpt_normal = trackable_utils.Checkpoint(var=v_normal_restore)
        ckpt_normal.restore(manager.latest_checkpoint)
        if agg == variable_scope.VariableAggregation.SUM:
            self.assertEqual(7.0, self.evaluate(v_normal_restore.read_value()))
        else:
            self.assertEqual(3.5, self.evaluate(v_normal_restore.read_value()))

        # Save normal, restore ONREAD
        ckpt = trackable_utils.Checkpoint(var=v_normal_save)
        manager = ckpt_manager.CheckpointManager(
            ckpt, "/tmp/ckpt_" + str(uuid.uuid4()), max_to_keep=None)
        manager.save()
        # Restores a value of 2/2 = 1.0 for SUM and 2.0 for MEAN.
        ckpt_on_read = trackable_utils.Checkpoint(var=v_on_read)
        ckpt_on_read.restore(manager.latest_checkpoint)
        if agg == variable_scope.VariableAggregation.SUM:
            self.assertEqual(1.0, self.evaluate(v_on_read._values[0]))
        else:
            self.assertEqual(2.0, self.evaluate(v_on_read._values[0]))
