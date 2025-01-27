# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/checkpoint_ops_test.py
ckpt_path = constant_op.constant(
    '/tmp/warm_starting_util_test5kl2a3pc/tmpph76tep2/model-0',
    shape=[],
    dtype=dtypes.string)
old_tensor_name = constant_op.constant(
    '/tmp/warm_starting_util_test5kl2a3pc/tmpph76tep2/model-0',
    shape=[],
    dtype=dtypes.string)
row_remapping = constant_op.constant(0, shape=[], dtype=dtypes.int64)
col_remapping = constant_op.constant(3, shape=[3], dtype=dtypes.int64)
initializing_values = constant_op.constant([],
                                           shape=[0, 1],
                                           dtype=dtypes.float32)
with self.cached_session(), self.assertRaisesRegex(
    (ValueError, errors.InvalidArgumentError), 'tensor must be 1-D'):
    self.evaluate(
        gen_checkpoint_ops.load_and_remap_matrix(
            ckpt_path=ckpt_path,
            old_tensor_name=old_tensor_name,
            row_remapping=row_remapping,
            col_remapping=col_remapping,
            initializing_values=initializing_values,
            num_rows=1,
            num_cols=1))
