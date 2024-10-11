# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable_test.py
with self.assertRaisesRegex(TypeError, 'should be a non-empty list of'):
    sharded_variable.ShardedVariable(None)

with self.assertRaisesRegex(TypeError, 'should be a non-empty list of'):
    sharded_variable.ShardedVariable(
        [variables_lib.Variable([0]), 'not-a-variable'])

with self.assertRaisesRegex(TypeError, 'should be a non-empty list of'):
    sharded_variable.ShardedVariable([])

with self.assertRaisesRegex(ValueError, 'must have the same dtype'):
    sharded_variable.ShardedVariable([
        variables_lib.Variable([0], dtype='int64'),
        variables_lib.Variable([1], dtype='int32')
    ])

with self.assertRaisesRegex(ValueError, 'the same shapes except'):
    sharded_variable.ShardedVariable([
        variables_lib.Variable(array_ops.ones((5, 10))),
        variables_lib.Variable(array_ops.ones((5, 20)))
    ])

with self.assertRaisesRegex(ValueError, '`SaveSliceInfo` should not'):
    v = variables_lib.Variable([0])
    v._set_save_slice_info(
        variables_lib.Variable.SaveSliceInfo(
            full_name='s', full_shape=[2], var_offset=[0], var_shape=[1]))
    sharded_variable.ShardedVariable([v])
