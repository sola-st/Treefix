# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
price_a = fc.numeric_column('price_a')
price_b = fc.numeric_column('price_b')
with ops.Graph().as_default():
    features = {
        'price_a': [[1.]],
        'price_b': [[3.]],
    }
    net1 = fc_old.input_layer(features, [price_a, price_b])
    net2 = fc_old.input_layer(features, [price_b, price_a])

    self.evaluate(variables_lib.global_variables_initializer())
    self.evaluate(lookup_ops.tables_initializer())

    self.assertAllClose([[1., 3.]], self.evaluate(net1))
    self.assertAllClose([[1., 3.]], self.evaluate(net2))
