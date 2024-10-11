# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
embedding_values = (
    (1., 2.),  # id 0
    (6., 7.),  # id 1
    (11., 12.)  # id 2
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
    country, dimension=2, initializer=_initializer)

# Provides 1-dim tensor and dense tensor.
features = {
    'price': array_ops.placeholder(dtypes.float32),
    'body-style': array_ops.sparse_placeholder(dtypes.string),
    # This is dense tensor for the categorical_column.
    'country': array_ops.placeholder(dtypes.string),
}
self.assertIsNone(features['price'].shape.ndims)
self.assertIsNone(features['body-style'].get_shape().ndims)
self.assertIsNone(features['country'].shape.ndims)

price_data = np.array([11., 12.])
body_style_data = sparse_tensor.SparseTensorValue(
    indices=((0,), (1,)),
    values=('sedan', 'hardtop'),
    dense_shape=(2,))
country_data = np.array([['US'], ['CA']])

net = fc.input_layer(features,
                     [price, one_hot_body_style, embedded_country])
self.assertEqual(1 + 3 + 2, net.shape[1])
with _initialized_session() as sess:

    # Each row is formed by concatenating `embedded_body_style`,
    # `one_hot_body_style`, and `price` in order.
    self.assertAllEqual(
        [[0., 0., 1., 1., 2., 11.], [1., 0., 0., 11., 12., 12.]],
        sess.run(
            net,
            feed_dict={
                features['price']: price_data,
                features['body-style']: body_style_data,
                features['country']: country_data
            }))
