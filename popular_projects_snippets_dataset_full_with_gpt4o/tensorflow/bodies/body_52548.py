# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
price = fc.numeric_column('price')
with ops.Graph().as_default():
    features1 = {'price': [[1.], [5.]]}
    features2 = {'price': [[2.], [10.]]}
    predictions1 = fc_old.linear_model(features1, [price])
    predictions2 = fc_old.linear_model(features2, [price])
    bias1 = get_linear_model_bias(name='linear_model')
    bias2 = get_linear_model_bias(name='linear_model_1')
    price_var1 = get_linear_model_column_var(price, name='linear_model')
    price_var2 = get_linear_model_column_var(price, name='linear_model_1')
    with _initialized_session() as sess:
        self.assertAllClose([0.], self.evaluate(bias1))
        sess.run(price_var1.assign([[10.]]))
        sess.run(bias1.assign([5.]))
        self.assertAllClose([[15.], [55.]], self.evaluate(predictions1))
        self.assertAllClose([0.], self.evaluate(bias2))
        sess.run(price_var2.assign([[10.]]))
        sess.run(bias2.assign([5.]))
        self.assertAllClose([[25.], [105.]], self.evaluate(predictions2))
