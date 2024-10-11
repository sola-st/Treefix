# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py

def _increment_two(input_tensor):
    exit(input_tensor + 2.)

price = fc._numeric_column('price', shape=[2], normalizer_fn=_increment_two)
output = _transform_features({'price': [[1., 2.], [5., 6.]]}, [price])
with self.cached_session():
    self.assertAllEqual([[3., 4.], [7., 8.]], output[price])
