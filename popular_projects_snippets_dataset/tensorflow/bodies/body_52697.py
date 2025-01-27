# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
# Github issue 12557
ids = fc.categorical_column_with_vocabulary_list(
    key='ids', vocabulary_list=('a', 'b', 'c'))
weights = fc.weighted_categorical_column(ids, 'weights')
indicator = fc.indicator_column(weights)
features = {
    'ids': constant_op.constant([['c', 'b', 'a', 'c']]),
    'weights': constant_op.constant([[2., 4., 6., 1.]])
}
indicator_tensor = fc._transform_features_v2(features, [indicator],
                                             None)[indicator]

self.evaluate(variables_lib.global_variables_initializer())
self.evaluate(lookup_ops.tables_initializer())

self.assertAllEqual([[6., 4., 3.]], self.evaluate(indicator_tensor))
