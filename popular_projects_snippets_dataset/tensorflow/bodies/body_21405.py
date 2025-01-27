# Extracted from ./data/repos/tensorflow/tensorflow/python/training/checkpoint_ops_test.py
ops.reset_default_graph()
# Create the checkpoint file in a temporary directory.
checkpoint_prefix = os.path.join(self.get_temp_dir(), 'model')
# 0., 1., ..., 79. reshaped into [5, 16].
initializer = init_ops.constant_initializer(
    np.reshape(np.linspace(0.0, 79, 5 * 16), (5, 16)))
with self.cached_session() as sess:
    with variable_scope.variable_scope('some_scope'):
        variable_scope.get_variable(name='embeddings', shape=[5, 16],
                                    initializer=initializer)
    self.evaluate(variables.global_variables_initializer())
    saver = saver_lib.Saver()
    saver.save(sess, checkpoint_prefix, global_step=5)
self.checkpoint_file = '{}-5'.format(checkpoint_prefix)

# Create the vocabulary files.
self.new_feature_vocab_file = os.path.join(
    self.get_temp_dir(), 'new_feature_vocab.txt')
with open(self.new_feature_vocab_file, 'w') as f:
    f.write('\n'.join(['zero', 'one', 'two', 'three', 'four']) + '\n')

self.old_feature_vocab_file = os.path.join(
    self.get_temp_dir(), 'old_feature_vocab.txt')
with open(self.old_feature_vocab_file, 'w') as f:
    f.write('\n'.join(['zero', 'one', 'two', 'three']) + '\n')

self.new_class_vocab_file = os.path.join(
    self.get_temp_dir(), 'new_class_vocab.txt')
with open(self.new_class_vocab_file, 'w') as f:
    f.write('\n'.join(['MISSING', 'knitting', 'flask', 'eminem']) + '\n')

self.old_class_vocab_file = os.path.join(
    self.get_temp_dir(), 'old_class_vocab.txt')
with open(self.old_class_vocab_file, 'w') as f:
    f.write('\n'.join(['knitting', 'eminem', 'MISSING']) + '\n')

self.init_val = 42

def _init_val_initializer(shape, dtype=None, partition_info=None):
    del dtype, partition_info  # Unused by this unit-testing initializer.
    exit(array_ops.tile(
        constant_op.constant([[self.init_val]], dtype=dtypes.float32), shape))

self.initializer = _init_val_initializer
