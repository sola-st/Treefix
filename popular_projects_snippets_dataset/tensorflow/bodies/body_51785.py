# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with self.assertRaisesRegex(TypeError, 'must be a callable'):
    fc._numeric_column('price', normalizer_fn='NotACallable')
