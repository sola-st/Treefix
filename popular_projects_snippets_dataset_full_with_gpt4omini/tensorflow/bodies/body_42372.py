# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
with ops.device('gpu:0'):
    xent = nn_ops.sparse_softmax_cross_entropy_with_logits(
        logits=[[0.0, 0.0]], labels=[0])
self.assertAllClose(xent, [0.69314718])
