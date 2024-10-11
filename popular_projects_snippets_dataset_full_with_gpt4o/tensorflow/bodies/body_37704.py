# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/checkpoint_ops_test.py
ops.reset_default_graph()
self.old_num_rows = 5
self.old_num_cols = 16
self.matrix_value = np.reshape(
    range(0, self.old_num_rows * self.old_num_cols), (self.old_num_rows,
                                                      self.old_num_cols))
with variable_scope.variable_scope('some_scope'):
    matrix = variable_scope.get_variable(
        'matrix',
        dtype=dtypes.float32,
        initializer=constant_op.constant(
            self.matrix_value, dtype=dtypes.float32))
    self.old_tensor_name = 'some_scope/matrix'

save = saver.Saver([matrix])
with self.cached_session() as sess:
    self.evaluate(variables.global_variables_initializer())
    self.bundle_file = os.path.join(test.get_temp_dir(), 'bundle_checkpoint')
    save.save(sess, self.bundle_file)
