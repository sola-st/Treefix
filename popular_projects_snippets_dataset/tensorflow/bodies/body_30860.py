# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/embedding_ops_test.py
with ops.Graph().as_default():
    p = variables.Variable(
        array_ops.zeros(shape=[100, 100], dtype=dtypes.float32))
    ids = constant_op.constant([0, 1, 1, 7], dtype=dtypes.int32)
    embedding_ops.embedding_lookup([p], ids)
