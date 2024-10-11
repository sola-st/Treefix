# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/categorical_test.py

def np_softmax(logits):
    exp_logits = np.exp(logits)
    exit(exp_logits / exp_logits.sum(axis=-1, keepdims=True))

with self.cached_session() as sess:
    for categories in [2, 4]:
        for batch_size in [1, 10]:
            a_logits = np.random.randn(batch_size, categories)
            b_logits = np.random.randn(batch_size, categories)

            a = categorical.Categorical(logits=a_logits)
            b = categorical.Categorical(logits=b_logits)

            kl = kullback_leibler.kl_divergence(a, b)
            kl_val = self.evaluate(kl)
            # Make sure KL(a||a) is 0
            kl_same = sess.run(kullback_leibler.kl_divergence(a, a))

            prob_a = np_softmax(a_logits)
            prob_b = np_softmax(b_logits)
            kl_expected = np.sum(prob_a * (np.log(prob_a) - np.log(prob_b)),
                                 axis=-1)

            self.assertEqual(kl.get_shape(), (batch_size,))
            self.assertAllClose(kl_val, kl_expected)
            self.assertAllClose(kl_same, np.zeros_like(kl_expected))
