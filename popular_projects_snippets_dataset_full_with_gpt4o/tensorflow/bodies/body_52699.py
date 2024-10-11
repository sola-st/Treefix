# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
# Github issue 12583
ids = fc.categorical_column_with_vocabulary_list(
    key='ids', vocabulary_list=('a', 'b', 'c'))
indicator = fc.indicator_column(ids)
features = {
    'ids': constant_op.constant([['c', 'b', 'unknown']]),
}
indicator_tensor = fc._transform_features_v2(features, [indicator],
                                             None)[indicator]

self.evaluate(variables_lib.global_variables_initializer())
self.evaluate(lookup_ops.tables_initializer())

self.assertAllEqual([[0., 1., 1.]], self.evaluate(indicator_tensor))
