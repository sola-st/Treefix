# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable_test.py
root = autotrackable.AutoTrackable()
v1 = variables_lib.Variable([3.])
v2 = variables_lib.Variable([2.])
root.v = sharded_variable.ShardedVariable([v1, v2])
root.train = def_function.function(
    lambda x: embedding_ops.embedding_lookup_v2(root.v.variables, x))
# TODO(b/144057383): Remove the necessity of root.serve once saving context
# is made to tf.function cache.
root.serve = def_function.function(
    lambda x: embedding_ops.embedding_lookup_v2(root.v.variables[0], x),
    input_signature=[tensor_spec.TensorSpec([2], dtypes.int32, name='x')])

# Trace and use root.train
self.assertAllEqual([3., 2.], root.train([0, 1]).numpy())

save_dir = os.path.join(self.get_temp_dir(), 'saved_model')
save.save(root, save_dir, root.serve)
self.assertAllEqual([3., 2.],
                    _load_and_run(save_dir, {'x': [0, 1]})['output_0'])

# Continue using root.train for training
self.assertAllEqual([3., 2.], root.train([0, 1]).numpy())
