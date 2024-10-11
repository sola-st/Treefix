# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_large_partitioned_variable_test.py
save_path = os.path.join(self.get_temp_dir(), "large_variable")
var_name = "my_var"
# Saving large partition variable.
with session.Session("", graph=ops.Graph()) as sess:
    with ops.device("/cpu:0"):
        # Create a partitioned variable which is larger than int32 size but
        # split into smaller sized variables.
        init = lambda shape, dtype, partition_info: constant_op.constant(
            True, dtype, shape)
        partitioned_var = list(variable_scope.get_variable(
            var_name,
            shape=[1 << 31],
            partitioner=partitioned_variables.fixed_size_partitioner(4),
            initializer=init,
            dtype=dtypes.bool))
        self.evaluate(variables.global_variables_initializer())
        save = saver.Saver(partitioned_var)
        val = save.save(sess, save_path)
        self.assertEqual(save_path, val)
