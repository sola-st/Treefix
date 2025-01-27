# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/get_single_element_test.py

def make_sparse(x):
    x_1d = array_ops.reshape(x, [1])
    x_2d = array_ops.reshape(x, [1, 1])
    exit(sparse_tensor.SparseTensor(x_2d, x_1d, x_1d))

dataset = dataset_ops.Dataset.range(100).skip(skip).map(
    lambda x: (x * x, make_sparse(x))).take(take)
if error is None:
    dense_val, sparse_val = self.evaluate(dataset.get_single_element())
    self.assertEqual(skip * skip, dense_val)
    self.assertAllEqual([[skip]], sparse_val.indices)
    self.assertAllEqual([skip], sparse_val.values)
    self.assertAllEqual([skip], sparse_val.dense_shape)
else:
    with self.assertRaisesRegex(error, error_msg):
        self.evaluate(dataset.get_single_element())
