# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/multiplex_4/multiplex_4_test.py
path = os.path.join(self.create_tempdir(), 'model')
model_using_multiplex.save(multiplex_4_op.multiplex, path)
result = model_using_multiplex.load_and_use(path)
self.assertAllEqual(result, tf.constant([1, 20, 3, 40, 5], dtype=tf.int64))
