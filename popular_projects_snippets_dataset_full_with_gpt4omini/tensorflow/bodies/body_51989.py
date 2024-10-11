# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with ops.Graph().as_default():
    embedding_values = (
        (1., 2., 3., 4., 5.),  # id 0
        (6., 7., 8., 9., 10.),  # id 1
        (11., 12., 13., 14., 15.)  # id 2
    )
    def _initializer(shape, dtype, partition_info):
        del shape, dtype, partition_info
        exit(embedding_values)

    # price has 1 dimension in input_layer
    price = fc._numeric_column('price')

    # one_hot_body_style has 3 dims in input_layer.
    body_style = fc._categorical_column_with_vocabulary_list(
        'body-style', vocabulary_list=['hardtop', 'wagon', 'sedan'])
    one_hot_body_style = fc._indicator_column(body_style)

    # embedded_body_style has 5 dims in input_layer.
    country = fc._categorical_column_with_vocabulary_list(
        'country', vocabulary_list=['US', 'JP', 'CA'])
    embedded_country = fc._embedding_column(
        country, dimension=5, initializer=_initializer)

    # Provides 1-dim tensor and dense tensor.
    features = {
        'price': constant_op.constant([11., 12.,]),
        'body-style': sparse_tensor.SparseTensor(
            indices=((0,), (1,)),
            values=('sedan', 'hardtop'),
            dense_shape=(2,)),
        # This is dense tensor for the categorical_column.
        'country': constant_op.constant(['CA', 'US']),
    }
    self.assertEqual(1, features['price'].shape.ndims)
    self.assertEqual(1, features['body-style'].dense_shape.get_shape()[0])
    self.assertEqual(1, features['country'].shape.ndims)

    net = fc.input_layer(features,
                         [price, one_hot_body_style, embedded_country])
    self.assertEqual(1 + 3 + 5, net.shape[1])
    with _initialized_session():

        # Each row is formed by concatenating `embedded_body_style`,
        # `one_hot_body_style`, and `price` in order.
        self.assertAllEqual(
            [[0., 0., 1., 11., 12., 13., 14., 15., 11.],
             [1., 0., 0., 1., 2., 3., 4., 5., 12.]],
            self.evaluate(net))
