# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/simple_hash_table/simple_hash_table_test.py
results = self._use_table(key_dtype, value_dtype)
self.assertAllClose(results, [-999, 100, -999])
