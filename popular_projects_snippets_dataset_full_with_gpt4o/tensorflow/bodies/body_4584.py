# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/simple_hash_table/simple_hash_table_test.py
table = simple_hash_table.SimpleHashTable(
    tf.int64, tf.int64, default_value=-1)
table.insert(1, 100)
table.insert(2, 200)
table.insert(3, 300)
keys, values = self.evaluate(table.export())
self.assertAllEqual(sorted(keys), [1, 2, 3])
self.assertAllEqual(sorted(values), [100, 200, 300])
