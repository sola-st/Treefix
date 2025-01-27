# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/sequence_feature_column_test.py
with self.assertRaisesRegex(TypeError, 'must be a callable'):
    sfc.sequence_numeric_column('aaa', normalizer_fn='NotACallable')
