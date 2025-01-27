# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
price = fc._numeric_column('price')
bucketized_price = fc._bucketized_column(price, boundaries=[0, 1])
builder = _LazyBuilder({
    'price':
        sparse_tensor.SparseTensor(
            indices=[[0, 0]], values=[0.3], dense_shape=[1, 1])
})
with self.assertRaisesRegex(ValueError, 'must be a Tensor'):
    bucketized_price._transform_feature(builder)
