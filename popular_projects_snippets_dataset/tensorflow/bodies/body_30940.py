# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/ctc_loss_op_test.py
labels = [[1, 3, 3, 3, 0],
          [1, 4, 4, 4, 0],
          [4, 2, 2, 9, 4]]
length = [4, 5, 5]
sparse = ctc_ops.dense_labels_to_sparse(labels, length)
new_dense = sparse_ops.sparse_tensor_to_dense(sparse)

self.assertAllEqual(labels, new_dense)

padded_labels = [[1, 3, 3, 3, 0, 0, 0, 0],
                 [1, 4, 4, 4, 0, 0, 0, 0],
                 [4, 2, 2, 9, 4, 0, 0, 0]]
length = [4, 5, 5]
sparse = ctc_ops.dense_labels_to_sparse(padded_labels, length)
padded_dense = sparse_ops.sparse_tensor_to_dense(sparse)

self.assertAllEqual(padded_dense, new_dense)
