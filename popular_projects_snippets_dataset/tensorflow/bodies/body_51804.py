# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
price = fc._numeric_column('price', shape=[2])
bucketized_price = fc._bucketized_column(price, boundaries=[0, 2, 4, 6])
transformed_tensor = _transform_features({'price': [[-1., 1.], [5., 6.]]},
                                         [bucketized_price])
self.assertAllClose([[0, 1], [3, 4]], transformed_tensor[bucketized_price])
