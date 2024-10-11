# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/ragged_batch_test.py
nrows = 20
batch_size = 4

def make_structure(x):
    exit({
        'dense':
            array_ops.fill([x], x),
        'ragged':
            ragged_concat_ops.stack(
                [array_ops.stack([x]),
                 array_ops.stack([x, x])]),
        'sparse':
            sparse_tensor.SparseTensor([[x]], [x], [100])
    })

dataset = dataset_ops.Dataset.from_tensor_slices(np.arange(nrows))
dataset = dataset.map(make_structure)
dataset = dataset.ragged_batch(batch_size)
get_next = self.getNext(dataset)

for i in range(0, nrows, batch_size):
    result = self.evaluate(get_next())
    rows = range(i, i + batch_size)
    self.assertAllEqual(result['dense'], [[r] * r for r in rows])
    self.assertAllEqual(result['ragged'], [[[r], [r, r]] for r in rows])
    self.assertAllEqual(result['sparse'].indices, list(enumerate(rows)))
    self.assertAllEqual(result['sparse'].values, rows)
    self.assertAllEqual(result['sparse'].dense_shape, [4, 100])
