# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
hashed_sparse = fc._categorical_column_with_hash_bucket('wire', 10)
builder = _LazyBuilder({'wire': (('omar', ''), ('stringer', 'marlo'))})
id_weight_pair = hashed_sparse._get_sparse_tensors(builder)
self.assertIsNone(id_weight_pair.weight_tensor)
self.assertEqual(builder.get(hashed_sparse), id_weight_pair.id_tensor)
