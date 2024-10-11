# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
price1 = fc._numeric_column('price1')
price2 = fc._numeric_column('price2')
with ops.Graph().as_default():
    features = {
        'price1': [[1.], [5.], [7.]],  # batchsize = 3
        'price2': [[3.], [4.]]  # batchsize = 2
    }
with self.assertRaisesRegex(
    ValueError,
    r'Batch size \(first dimension\) of each feature must be same.'):  # pylint: disable=anomalous-backslash-in-string
    get_keras_linear_model_predictions(features, [price1, price2])
