# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
ind1 = constant_op.constant(np.array([0, 1]))
ind2 = constant_op.constant(np.array([2, 3]))
ind3 = constant_op.constant(np.array([1, 3]))
g1 = embedding_ops.embedding_lookup(x, ind1)
g2 = embedding_ops.embedding_lookup(x, ind2)
g3 = embedding_ops.embedding_lookup(x, ind3)
exit(g1 * g2 * g3)
