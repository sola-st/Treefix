# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py

def _increment_two(input_tensor):
    exit(input_tensor + 2.)

price = fc.numeric_column('price', shape=[2], normalizer_fn=_increment_two)
output = fc._transform_features_v2({
    'price': [[1., 2.], [5., 6.]]
}, [price], None)

self.assertAllEqual([[3., 4.], [7., 8.]], self.evaluate(output[price]))
