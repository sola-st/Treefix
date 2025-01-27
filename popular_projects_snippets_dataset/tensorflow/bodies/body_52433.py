# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
"""Tests _get_dense_tensor() for input with shape=[1]."""
price = fc.numeric_column('price', shape=[1])
bucketized_price = fc.bucketized_column(price, boundaries=[0, 2, 4, 6])
with ops.Graph().as_default():
    transformation_cache = fc.FeatureTransformationCache({
        'price': [[-1.], [1.], [5.], [6.]]
    })

    self.evaluate(variables_lib.global_variables_initializer())
    self.evaluate(lookup_ops.tables_initializer())

    bucketized_price_tensor = bucketized_price.get_dense_tensor(
        transformation_cache, None)
    self.assertAllClose(
        # One-hot tensor.
        [[[1., 0., 0., 0., 0.]], [[0., 1., 0., 0., 0.]],
         [[0., 0., 0., 1., 0.]], [[0., 0., 0., 0., 1.]]],
        self.evaluate(bucketized_price_tensor))
