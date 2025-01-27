# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/simple_hash_table/simple_hash_table_test.py
table = simple_hash_table.SimpleHashTable(
    tf.int64, tf.int64, default_value=-1)
keys = tf.constant([1, 2, 3], dtype=tf.int64)
values = tf.constant([100, 200, 300], dtype=tf.int64)
table.do_import(keys, values)
self.assertEqual(table.find(1), 100)
self.assertEqual(table.find(2), 200)
self.assertEqual(table.find(3), 300)
self.assertEqual(table.find(9), -1)
