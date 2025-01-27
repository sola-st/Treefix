# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
price1 = fc.numeric_column('price1', shape=2)
price2 = fc.numeric_column('price2')
with ops.Graph().as_default():
    features = {'price1': [[1., 2.], [5., 6.]], 'price2': [[3.], [4.]]}
    cols_to_vars = {}
    fc_old.linear_model(features, [price1, price2], cols_to_vars=cols_to_vars)
    bias = get_linear_model_bias()
    price1_var = get_linear_model_column_var(price1)
    price2_var = get_linear_model_column_var(price2)
    self.assertEqual(cols_to_vars['bias'], [bias])
    self.assertEqual(cols_to_vars[price1], [price1_var])
    self.assertEqual(cols_to_vars[price2], [price2_var])
