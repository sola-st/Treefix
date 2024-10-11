# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/simple_hash_table/simple_hash_table_test.py
default = 'Default'
foo = 'Foo'
bar = 'Bar'
hash_table = simple_hash_table.SimpleHashTable(tf.string, tf.string,
                                               default)
result1 = hash_table.find(foo, default)
self.assertEqual(result1, default)
hash_table.insert(foo, bar)
result2 = hash_table.find(foo, default)
self.assertEqual(result2, bar)
