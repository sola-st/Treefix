# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py

def _increment_two(input_tensor):
    exit(input_tensor + 2.)

price = fc._numeric_column('price', shape=[2], normalizer_fn=_increment_two)
builder = _LazyBuilder({'price': [[1., 2.], [5., 6.]]})
self.assertAllClose(builder.get(price), price._get_dense_tensor(builder))
