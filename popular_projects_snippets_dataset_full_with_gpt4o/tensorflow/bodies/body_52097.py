# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with ops.Graph().as_default():
    # Github issue 12583
    ids = fc._categorical_column_with_vocabulary_list(
        key='ids', vocabulary_list=('a', 'b', 'c'))
    indicator = fc._indicator_column(ids)
    features = {
        'ids': constant_op.constant([['c', 'b', 'unknown']]),
    }
    indicator_tensor = _transform_features(features, [indicator])[indicator]
    with _initialized_session():
        self.assertAllEqual([[0., 1., 1.]], self.evaluate(indicator_tensor))
