# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with ops.Graph().as_default():
    a = fc._categorical_column_with_vocabulary_list(
        key='aaa', vocabulary_list=('omar', 'stringer', 'marlo'))
    a_indicator = fc._indicator_column(a)
    features = {
        'aaa': sparse_tensor.SparseTensorValue(
            indices=((0, 0), (1, 0), (1, 1)),
            values=('marlo', 'skywalker', 'omar'),
            dense_shape=(2, 2))
    }
    indicator_tensor = _transform_features(features,
                                           [a_indicator])[a_indicator]
    with _initialized_session():
        self.assertAllEqual([[0, 0, 1], [1, 0, 0]],
                            self.evaluate(indicator_tensor))
