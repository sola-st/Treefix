# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
price = fc._numeric_column('price')
with ops.Graph().as_default() as g:
    features = {'price': [[1.], [5.]]}
    fc.linear_model(features, [price], trainable=False)
    trainable_vars = g.get_collection(ops.GraphKeys.TRAINABLE_VARIABLES)
    self.assertEqual([], trainable_vars)
