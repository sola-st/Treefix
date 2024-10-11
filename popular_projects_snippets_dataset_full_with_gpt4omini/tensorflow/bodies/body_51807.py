# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
"""Tests _get_sparse_tensors() for input with shape=[1]."""
price = fc._numeric_column('price', shape=[1])
bucketized_price = fc._bucketized_column(price, boundaries=[0, 2, 4, 6])
with ops.Graph().as_default():
    builder = _LazyBuilder({'price': [[-1.], [1.], [5.], [6.]]})
    with _initialized_session() as sess:
        id_weight_pair = bucketized_price._get_sparse_tensors(builder)
        self.assertIsNone(id_weight_pair.weight_tensor)
        id_tensor_value = sess.run(id_weight_pair.id_tensor)
        self.assertAllEqual(
            [[0, 0], [1, 0], [2, 0], [3, 0]], id_tensor_value.indices)
        self.assertAllEqual([0, 1, 3, 4], id_tensor_value.values)
        self.assertAllEqual([4, 1], id_tensor_value.dense_shape)
