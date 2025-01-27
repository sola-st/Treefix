# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input_test.py
with ops.Graph().as_default():
    sparse = sparse_tensor.SparseTensor(
        indices=array_ops.placeholder(dtypes.int64),
        values=array_ops.placeholder(dtypes.float32),
        dense_shape=array_ops.placeholder(dtypes.int64))
    self.assertIs(None, sparse.dense_shape.get_shape().num_elements())
    batched = inp.maybe_batch([sparse],
                              keep_input=True,
                              batch_size=2,
                              enqueue_many=True)
    self.assertIs(None, batched.dense_shape.get_shape().num_elements())
