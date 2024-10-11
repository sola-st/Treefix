# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
price = fc._numeric_column('price', shape=[2])
bucketized_price = fc._bucketized_column(price, boundaries=[0, 50])
hash_bucket_size = 10
price_cross_wire = fc._crossed_column([bucketized_price, 'wire'],
                                      hash_bucket_size)
features = {
    'price': constant_op.constant([[1., 2.], [5., 6.]]),
    'wire': sparse_tensor.SparseTensor(
        values=['omar', 'stringer', 'marlo'],
        indices=[[0, 0], [1, 0], [1, 1]],
        dense_shape=[2, 2]),
}
outputs = _transform_features(features, [price_cross_wire])
output = outputs[price_cross_wire]
output_val = self.evaluate(output)
self.assertAllEqual([[0, 0], [0, 1], [1, 0], [1, 1], [1, 2], [1, 3]],
                    output_val.indices)
for val in output_val.values:
    self.assertIn(val, list(range(hash_bucket_size)))
self.assertAllEqual([2, 4], output_val.dense_shape)
