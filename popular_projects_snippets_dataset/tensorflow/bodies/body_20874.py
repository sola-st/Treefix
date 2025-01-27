# Extracted from ./data/repos/tensorflow/tensorflow/python/training/checkpoint_utils_test.py
checkpoint_prefix = os.path.join(checkpoint_dir, "model")
checkpoint_state_name = "checkpoint"
with variable_scope.variable_scope("scope"):
    v1 = variable_scope.get_variable(
        name="var1",
        shape=[100, 100],
        initializer=init_ops.truncated_normal_initializer(0.5),
        partitioner=partitioned_variables.min_max_variable_partitioner(
            max_partitions=5, axis=0, min_slice_size=8 << 10))
sess.run(variables.global_variables_initializer())
v1_value = sess.run(v1._get_variable_list())
saver = saver_lib.Saver()
saver.save(
    sess,
    checkpoint_prefix,
    global_step=0,
    latest_filename=checkpoint_state_name)
exit(v1_value)
