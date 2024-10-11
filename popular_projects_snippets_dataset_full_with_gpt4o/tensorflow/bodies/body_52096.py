# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with ops.Graph().as_default():
    # Github issue 12583
    ids = fc._categorical_column_with_vocabulary_list(
        key='ids', vocabulary_list=('a', 'b', 'c'))
    weights = fc._weighted_categorical_column(ids, 'weights')
    indicator = fc._indicator_column(weights)
    features = {
        'ids': constant_op.constant([['c', 'b', 'unknown']]),
        'weights': constant_op.constant([[2., 4., 6.]])
    }
    indicator_tensor = _transform_features(features, [indicator])[indicator]
    with _initialized_session():
        self.assertAllEqual([[0., 4., 2.]], self.evaluate(indicator_tensor))
