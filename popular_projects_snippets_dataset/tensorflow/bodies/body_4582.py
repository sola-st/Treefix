# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/simple_hash_table/simple_hash_table_test.py
results = def_function.function(
    lambda: self._use_table(key_dtype, value_dtype))
self.assertAllClose(self.evaluate(results), [-999.0, 100.0, -999.0])
