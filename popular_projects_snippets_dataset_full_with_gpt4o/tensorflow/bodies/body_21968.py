# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input_test.py
with ops.Graph().as_default():
    sparse = sparse_tensor.SparseTensor(
        indices=[[0], [0]], values=[1.0, 2.0], dense_shape=[2])
    self.assertAllEqual((1,), sparse.dense_shape.get_shape().as_list())
    batched = inp.maybe_shuffle_batch_join([[sparse]],
                                           2,
                                           10,
                                           1, [True, False],
                                           enqueue_many=True)
    self.assertAllEqual((1,), batched.dense_shape.get_shape().as_list())
