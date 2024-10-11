# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
price = fc.numeric_column('price')
with ops.Graph().as_default() as g:
    features = {'price': [[1.], [5.]]}
    fc_old.linear_model(features, [price])
    bias = get_linear_model_bias()
    price_var = get_linear_model_column_var(price)
    trainable_vars = g.get_collection(ops.GraphKeys.TRAINABLE_VARIABLES)
    self.assertIn(bias, trainable_vars)
    self.assertIn(price_var, trainable_vars)
