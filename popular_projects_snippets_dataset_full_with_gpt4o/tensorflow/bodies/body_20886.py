# Extracted from ./data/repos/tensorflow/tensorflow/python/training/checkpoint_utils_test.py
checkpoint_dir = self.get_temp_dir()
with self.cached_session() as session:
    v1 = _create_partition_checkpoints(session, checkpoint_dir)

# New graph and session.
with ops.Graph().as_default() as g:
    with self.session(graph=g) as session:
        with variable_scope.variable_scope("some_scope"):
            my1 = variable_scope.get_variable(
                name="my1",
                shape=[100, 100],
                initializer=init_ops.zeros_initializer(),
                partitioner=partitioned_variables.min_max_variable_partitioner(
                    max_partitions=5, axis=0, min_slice_size=8 << 10))
            my1_var_list = my1._get_variable_list()
        # Create another variable with different partitions than the variable in
        # the checkpoint.
        with variable_scope.variable_scope("some_other_scope"):
            my2 = variable_scope.get_variable(
                name="var1",
                shape=[100, 100],
                initializer=init_ops.zeros_initializer(),
                partitioner=partitioned_variables.min_max_variable_partitioner(
                    max_partitions=5, axis=0, min_slice_size=16 << 10))
            my2_var_list = my2._get_variable_list()

        checkpoint_utils.init_from_checkpoint(checkpoint_dir, {
            "scope/var1": "some_scope/my1",
            "scope/": "some_other_scope/"})

        session.run(variables.global_variables_initializer())
        my1_values = session.run(my1_var_list)
        self.assertAllEqual(my1_values, v1)
        my2_values = session.run(my2_var_list)
        # Verify we created different number of partitions.
        self.assertNotEquals(len(my2_values), len(v1))
        # Verify the values were correctly initialized inspite of different
        # partitions.
        full_my2_values = np.concatenate(my2_values, axis=0)
        full_v1_values = np.concatenate(v1, axis=0)
        self.assertAllEqual(full_my2_values, full_v1_values)

    # New graph and session.
with ops.Graph().as_default() as g:
    with self.session(graph=g) as session:
        with variable_scope.variable_scope("some_scope"):
            my1 = variable_scope.get_variable(
                name="my1",
                shape=[100, 100],
                initializer=init_ops.truncated_normal_initializer(0.5),
                partitioner=partitioned_variables.min_max_variable_partitioner(
                    max_partitions=5, axis=0, min_slice_size=8 << 10))
            my1_var_list = my1._get_variable_list()

        checkpoint_utils.init_from_checkpoint(checkpoint_dir,
                                              {"scope/var1": my1_var_list,})

        session.run(variables.global_variables_initializer())
        my1_values = session.run(my1_var_list)
        self.assertAllEqual(my1_values, v1)
