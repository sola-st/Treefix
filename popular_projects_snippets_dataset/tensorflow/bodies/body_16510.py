# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_xent_test.py
with self.assertRaisesRegex(ValueError, "must have the same shape"):
    nn_impl.sigmoid_cross_entropy_with_logits(labels=[1, 2, 3],
                                              logits=[[2, 1]])
