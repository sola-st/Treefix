# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
builder = _LazyBuilder(features={'a': [[2], [3.]]})
with self.assertRaisesRegex(ValueError,
                            'bbb is not in features dictionary'):
    builder.get('bbb')
with self.assertRaisesRegex(ValueError,
                            'bbb is not in features dictionary'):
    builder.get(u'bbb')
