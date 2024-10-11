# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
animal = fc._indicator_column(
    fc._categorical_column_with_identity('animal', num_buckets=4))

builder = _LazyBuilder({
    'animal':
        sparse_tensor.SparseTensor(
            indices=[[0, 0], [0, 1]], values=[1, 1], dense_shape=[1, 2])
})
output = builder.get(animal)
with self.cached_session():
    self.assertAllEqual([[0., 2., 0., 0.]], self.evaluate(output))
