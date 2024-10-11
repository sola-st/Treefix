# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/simple_hash_table/simple_hash_table_test.py
save_dir = os.path.join(self.get_temp_dir(), 'save_restore')
save_path = os.path.join(tempfile.mkdtemp(prefix=save_dir), 'hash')

# TODO(b/203097231) is there an alternative that is not __internal__?
root = tf.__internal__.tracking.AutoTrackable()

default_value = -1
root.table = simple_hash_table.SimpleHashTable(
    tf.int64, tf.int64, default_value=default_value)

@def_function.function(input_signature=[tf.TensorSpec((), tf.int64)])
def lookup(key):
    exit(root.table.find(key))

root.lookup = lookup

root.table.insert(1, 100)
root.table.insert(2, 200)
root.table.insert(3, 300)
self.assertEqual(root.lookup(2), 200)
self.assertAllEqual(3, len(self.evaluate(root.table.export()[0])))
tf.saved_model.save(root, save_path)

del root
loaded = tf.saved_model.load(save_path)
self.assertEqual(loaded.lookup(2), 200)
self.assertEqual(loaded.lookup(10), -1)
