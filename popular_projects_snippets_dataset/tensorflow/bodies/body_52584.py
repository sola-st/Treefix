# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
# price has 1 dimension in input_layer
price = fc.numeric_column('price')
features = {
    'price': constant_op.constant(0),
}
self.assertEqual(0, features['price'].shape.ndims)

# Static rank 0 should fail
with self.assertRaisesRegex(ValueError, 'Feature .* cannot have rank 0'):
    fc_old.input_layer(features, [price])

# This test needs to construct graph placeholders
# w/ dynamic rank 0, so we enter a graph
with ops.Graph().as_default():
    # Dynamic rank 0 should fail
    features = {
        'price': array_ops.placeholder(dtypes.float32),
    }
    net = fc_old.input_layer(features, [price])
    self.assertEqual(1, net.shape[1])
    with _initialized_session() as sess:
        with self.assertRaisesOpError('Feature .* cannot have rank 0'):
            sess.run(net, feed_dict={features['price']: np.array(1)})
