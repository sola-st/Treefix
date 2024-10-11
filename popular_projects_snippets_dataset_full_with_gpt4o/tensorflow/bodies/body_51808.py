# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
"""Tests _get_sparse_tensors() for input with shape=[2]."""
price = fc._numeric_column('price', shape=[2])
bucketized_price = fc._bucketized_column(price, boundaries=[0, 2, 4, 6])
with ops.Graph().as_default():
    builder = _LazyBuilder({'price': [[-1., 1.], [5., 6.]]})
    with _initialized_session() as sess:
        id_weight_pair = bucketized_price._get_sparse_tensors(builder)
        self.assertIsNone(id_weight_pair.weight_tensor)
        id_tensor_value = sess.run(id_weight_pair.id_tensor)
        self.assertAllEqual(
            [[0, 0], [0, 1], [1, 0], [1, 1]], id_tensor_value.indices)
        # Values 0-4 correspond to the first column of the input price.
        # Values 5-9 correspond to the second column of the input price.
        self.assertAllEqual([0, 6, 3, 9], id_tensor_value.values)
        self.assertAllEqual([2, 2], id_tensor_value.dense_shape)
