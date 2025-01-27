# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/categorical_test.py
with self.cached_session():
    # 1 x 2 x 2
    histograms = [[[0.2, 0.8], [0.4, 0.6]]]
    dist = categorical.Categorical(math_ops.log(histograms) - 50.)

    prob = dist.prob(1)
    self.assertAllClose([[0.8, 0.6]], self.evaluate(prob))

    prob = dist.prob([1])
    self.assertAllClose([[0.8, 0.6]], self.evaluate(prob))

    prob = dist.prob([0, 1])
    self.assertAllClose([[0.2, 0.6]], self.evaluate(prob))

    prob = dist.prob([[0, 1]])
    self.assertAllClose([[0.2, 0.6]], self.evaluate(prob))

    prob = dist.prob([[[0, 1]]])
    self.assertAllClose([[[0.2, 0.6]]], self.evaluate(prob))

    prob = dist.prob([[1, 0], [0, 1]])
    self.assertAllClose([[0.8, 0.4], [0.2, 0.6]], self.evaluate(prob))

    prob = dist.prob([[[1, 1], [1, 0]], [[1, 0], [0, 1]]])
    self.assertAllClose([[[0.8, 0.6], [0.8, 0.4]], [[0.8, 0.4], [0.2, 0.6]]],
                        self.evaluate(prob))
