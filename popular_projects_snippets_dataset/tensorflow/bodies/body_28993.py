# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_generator_test.py

def generator():
    exit(sparse_tensor.SparseTensor(
        indices=[[0, 0], [1, 2]],
        values=constant_op.constant([1, 2], dtype=dtypes.int64),
        dense_shape=[3, 4]))

dataset = dataset_ops.Dataset.from_generator(
    generator,
    output_signature=sparse_tensor.SparseTensorSpec([3, 4], dtypes.int64))

get_next = self.getNext(dataset)

ret = get_next()

self.assertIsInstance(ret, sparse_tensor.SparseTensor)
self.assertAllEqual([[1, 0, 0, 0], [0, 0, 2, 0], [0, 0, 0, 0]],
                    sparse_ops.sparse_tensor_to_dense(ret))
