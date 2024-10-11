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

# Provides 1-dim tensor and dense tensor.
features = {
    'price': constant_op.constant([-1., 12.,]),
    'body-style': sparse_tensor.SparseTensor(
        indices=((0,), (1,)),
        values=('sedan', 'hardtop'),
        dense_shape=(2,)),
}
self.assertEqual(1, features['price'].shape.ndims)
self.assertEqual(1, features['body-style'].dense_shape.get_shape()[0])

net = fc.linear_model(features, [price_buckets, body_style])
with _initialized_session() as sess:
    bias = get_linear_model_bias()
    price_buckets_var = get_linear_model_column_var(price_buckets)
    body_style_var = get_linear_model_column_var(body_style)

    sess.run(price_buckets_var.assign([[10.], [100.], [1000.], [10000.]]))
    sess.run(body_style_var.assign([[-10.], [-100.], [-1000.]]))
    sess.run(bias.assign([5.]))

    self.assertAllClose([[10 - 1000 + 5.], [1000 - 10 + 5.]],
                        self.evaluate(net))
