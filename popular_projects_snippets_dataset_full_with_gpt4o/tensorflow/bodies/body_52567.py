# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
price = fc.numeric_column('price', shape=2)
with ops.Graph().as_default():
    features = {'price': [[1.], [5.]]}
    with self.assertRaisesRegex(
        Exception,
        r'Cannot reshape a tensor with 2 elements to shape \[2,2\]'):
        fc_old.input_layer(features, [price])
