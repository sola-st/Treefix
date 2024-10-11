# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
price = fc._numeric_column('price')
price_buckets = fc._bucketized_column(
    price, boundaries=[
        0.,
        10.,
        100.,
    ])
body_style = fc._categorical_column_with_vocabulary_list(
    'body-style', vocabulary_list=['hardtop', 'wagon', 'sedan'])
country = fc._categorical_column_with_vocabulary_list(
    'country', vocabulary_list=['US', 'JP', 'CA'])

# Provides 1-dim tensor and dense tensor.
features = {
    'price': array_ops.placeholder(dtypes.float32),
    'body-style': array_ops.sparse_placeholder(dtypes.string),
    'country': array_ops.placeholder(dtypes.string),
}
self.assertIsNone(features['price'].shape.ndims)
self.assertIsNone(features['body-style'].get_shape().ndims)

price_data = np.array([-1., 12.])
body_style_data = sparse_tensor.SparseTensorValue(
    indices=((0,), (1,)),
    values=('sedan', 'hardtop'),
    dense_shape=(2,))
country_data = np.array(['US', 'CA'])

net = fc.linear_model(features, [price_buckets, body_style, country])
bias = get_linear_model_bias()
price_buckets_var = get_linear_model_column_var(price_buckets)
body_style_var = get_linear_model_column_var(body_style)
with _initialized_session() as sess:
    sess.run(price_buckets_var.assign([[10.], [100.], [1000.], [10000.]]))
    sess.run(body_style_var.assign([[-10.], [-100.], [-1000.]]))
    sess.run(bias.assign([5.]))

    self.assertAllClose([[10 - 1000 + 5.], [1000 - 10 + 5.]],
                        sess.run(
                            net,
                            feed_dict={
                                features['price']: price_data,
                                features['body-style']: body_style_data,
                                features['country']: country_data
                            }))
