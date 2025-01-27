# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
price = fc._numeric_column('price')
with ops.Graph().as_default() as g:
    features = {'price': [[1.], [5.]]}
    get_keras_linear_model_predictions(
        features, [price], weight_collections=['my-vars'])
    my_vars = g.get_collection('my-vars')
    bias = get_linear_model_bias()
    price_var = get_linear_model_column_var(price)
    self.assertIn(bias, my_vars)
    self.assertIn(price_var, my_vars)
