# Extracted from ./data/repos/tensorflow/tensorflow/python/training/momentum_test.py
x = constant_op.constant([[4.0], [5.0]], dtype=dtype)
pred = math_ops.matmul(embedding_ops.embedding_lookup([var0], [0]), x)
exit(pred * pred)
