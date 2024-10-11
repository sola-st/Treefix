# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
price1 = fc._numeric_column('price1', shape=2)
price2 = fc._numeric_column('price2', shape=3)
with ops.Graph().as_default():
    features = {
        'price1': [[1., 2.], [6., 7.]],
        'price2': [[3., 4., 5.], [8., 9., 10.]]
    }
    cols_to_vars = {}
    with variable_scope.variable_scope(
        'linear',
        partitioner=partitioned_variables.fixed_size_partitioner(2, axis=0)):
        fc.linear_model(features, [price1, price2], cols_to_vars=cols_to_vars)
    with _initialized_session():
        self.assertEqual([0.], cols_to_vars['bias'][0].eval())
        # Partitioning shards the [2, 1] price1 var into 2 [1, 1] Variables.
        self.assertAllEqual([[0.]], cols_to_vars[price1][0])
        self.assertAllEqual([[0.]], cols_to_vars[price1][1])
        # Partitioning shards the [3, 1] price2 var into a [2, 1] Variable and
        # a [1, 1] Variable.
        self.assertAllEqual([[0.], [0.]], cols_to_vars[price2][0])
        self.assertAllEqual([[0.]], cols_to_vars[price2][1])
