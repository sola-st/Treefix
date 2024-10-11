# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/categorical_test.py
with self.cached_session() as sess:
    logits = constant_op.constant([[1., 2., 3.], [2., 5., 1.]])

    probabilities = nn_ops.softmax(logits)
    log_probabilities = nn_ops.log_softmax(logits)
    true_entropy = - math_ops.reduce_sum(
        probabilities * log_probabilities, axis=-1)

    categorical_distribution = categorical.Categorical(probs=probabilities)
    categorical_entropy = categorical_distribution.entropy()

    # works
    true_entropy_g = gradients_impl.gradients(true_entropy, [logits])
    categorical_entropy_g = gradients_impl.gradients(
        categorical_entropy, [logits])

    res = sess.run({"true_entropy": true_entropy,
                    "categorical_entropy": categorical_entropy,
                    "true_entropy_g": true_entropy_g,
                    "categorical_entropy_g": categorical_entropy_g})
    self.assertAllClose(res["true_entropy"],
                        res["categorical_entropy"])
    self.assertAllClose(res["true_entropy_g"],
                        res["categorical_entropy_g"])
