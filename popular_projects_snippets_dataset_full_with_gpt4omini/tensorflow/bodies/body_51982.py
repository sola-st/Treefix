# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
price1 = fc._numeric_column('price1')
price2 = fc._numeric_column('price2')
price3 = fc._numeric_column('price3')
with ops.Graph().as_default():
    features = {
        'price1': array_ops.placeholder(dtype=dtypes.int64),  # batchsize = 3
        'price2': [[3.], [4.]],  # batchsize = 2
        'price3': [[3.], [4.], [5.]]  # batchsize = 3
    }
    with self.assertRaisesRegex(
        ValueError,
        r'Batch size \(first dimension\) of each feature must be same.'):  # pylint: disable=anomalous-backslash-in-string
        fc.input_layer(features, [price1, price2, price3])
