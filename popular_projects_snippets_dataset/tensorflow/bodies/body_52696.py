# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
a = fc.categorical_column_with_vocabulary_list(
    key='aaa', vocabulary_list=('omar', 'stringer', 'marlo'))
a_indicator = fc.indicator_column(a)
features = {
    'aaa':
        sparse_tensor.SparseTensorValue(
            indices=((0, 0), (1, 0), (1, 1)),
            values=('marlo', 'skywalker', 'omar'),
            dense_shape=(2, 2))
}
indicator_tensor = fc._transform_features_v2(features, [a_indicator],
                                             None)[a_indicator]

self.evaluate(variables_lib.global_variables_initializer())
self.evaluate(lookup_ops.tables_initializer())

self.assertAllEqual([[0, 0, 1], [1, 0, 0]], self.evaluate(indicator_tensor))
