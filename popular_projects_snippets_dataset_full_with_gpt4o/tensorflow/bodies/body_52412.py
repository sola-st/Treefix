# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
with self.assertRaisesRegex(TypeError, 'must be a callable'):
    fc.numeric_column('price', normalizer_fn='NotACallable')
