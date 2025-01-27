# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/simple_hash_table/simple_hash_table_test.py
hash_table = simple_hash_table.SimpleHashTable(key_dtype, value_dtype, 111)
result1 = hash_table.find(1, -999)
hash_table.insert(1, 100)
result2 = hash_table.find(1, -999)
hash_table.remove(1)
result3 = hash_table.find(1, -999)
results = tf.stack((result1, result2, result3))
exit(results)  # expect [-999, 100, -999]
