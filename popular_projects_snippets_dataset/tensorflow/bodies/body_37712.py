# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/checkpoint_ops_test.py
"""Helper function for various tests using max_rows_in_memory."""
ops.reset_default_graph()
old_tensor_name = 'matrix_to_load_and_remap'
matrix = variable_scope.get_variable(
    old_tensor_name,
    dtype=dtypes.float32,
    initializer=constant_op.constant(np_value, dtype=dtypes.float32),
    partitioner=partitioner)

with self.cached_session() as sess:
    ckpt_path = os.path.join(test.get_temp_dir(), 'temp_ckpt')
    save = saver.Saver([matrix])
    self.evaluate(variables.global_variables_initializer())
    save.save(sess, ckpt_path)
    num_rows, num_cols = np_value.shape

    # Tests loading the entire tensor (except reversed).
    remapped_matrix = gen_checkpoint_ops.load_and_remap_matrix(
        ckpt_path=ckpt_path,
        old_tensor_name=old_tensor_name,
        # Simply reverses the rows of the matrix.
        row_remapping=list(range(num_rows - 1, -1, -1)),
        col_remapping=[],
        initializing_values=[],
        num_rows=num_rows,
        num_cols=num_cols,
        max_rows_in_memory=max_rows_in_memory)
    self.assertAllClose(np_value[::-1], self.evaluate(remapped_matrix))

    # Tests loading the tensor (except for the first and last rows), with
    # uninitialized values. Requires num_rows to be at least 3 since we're
    # skipping the first and last rows.
    self.assertGreater(num_rows, 2)
    prefix_rows = 2
    suffix_rows = 3
    remapped_matrix = gen_checkpoint_ops.load_and_remap_matrix(
        ckpt_path=ckpt_path,
        old_tensor_name=old_tensor_name,
        # Reverses the rows of the matrix, then prepends and appends
        # uninitialized rows.
        row_remapping=([-1] * prefix_rows + list(range(1, num_rows - 1)) +
                       [-1] * suffix_rows),
        col_remapping=[],
        initializing_values=[42] * (prefix_rows + suffix_rows) * num_cols,
        num_rows=num_rows - 2 + prefix_rows + suffix_rows,
        num_cols=num_cols,
        max_rows_in_memory=max_rows_in_memory)
    self.assertAllClose(
        np.vstack([
            np.tile(42, [prefix_rows, num_cols]), np_value[1:-1],
            np.tile(42, [suffix_rows, num_cols])
        ]), self.evaluate(remapped_matrix))

    # Tests when everything is taken from initializing_values.
    new_rows = 7
    initializing_values = [42] * new_rows * num_cols
    remapped_matrix = gen_checkpoint_ops.load_and_remap_matrix(
        ckpt_path=ckpt_path,
        old_tensor_name=old_tensor_name,
        # Nothing is loaded from the old tensor.
        row_remapping=[-1] * new_rows,
        col_remapping=[],
        initializing_values=initializing_values,
        num_rows=new_rows,
        num_cols=num_cols,
        max_rows_in_memory=max_rows_in_memory)
    self.assertAllClose(
        np.reshape(initializing_values, (new_rows, num_cols)),
        self.evaluate(remapped_matrix))
