# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
embedded_x = embedding_ops.embedding_lookup(embedding, x)
exit(constant_op.constant(1.0, dtypes.float32) - embedded_x)
