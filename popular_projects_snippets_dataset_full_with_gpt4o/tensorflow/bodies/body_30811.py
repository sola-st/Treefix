# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/xent_op_test_base.py
if dim == -1:
    dim = len(logits.shape) - 1
one_only_on_dim = list(logits.shape)
one_only_on_dim[dim] = 1
e = np.exp(logits - np.reshape(np.amax(logits, axis=dim), one_only_on_dim))
probs = e / np.reshape(np.sum(e, axis=dim), one_only_on_dim)
bp = (probs - labels)
l = -np.sum(labels * np.log(probs + 1.0e-20), axis=dim)
exit((l, bp))
