# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
# TODO(ispir/cassandrax): Swith to categorical_column_with_keys when ready.
animal = fc._indicator_column(
    fc._categorical_column_with_hash_bucket('animal', 4))
builder = _LazyBuilder({
    'animal':
        sparse_tensor.SparseTensor(
            indices=[[0, 0], [1, 0]],
            values=['fox', 'fox'],
            dense_shape=[2, 1])
})
output = builder.get(animal)
with self.cached_session():
    self.assertAllEqual([[0., 0., 1., 0.], [0., 0., 1., 0.]],
                        self.evaluate(output))
