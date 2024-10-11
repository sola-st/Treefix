# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/bernoulli_test.py
invalid_ps = [1.01, 2.]
for p in invalid_ps:
    with self.assertRaisesOpError("probs has components greater than 1"):
        dist = bernoulli.Bernoulli(probs=p, validate_args=True)
        self.evaluate(dist.probs)

invalid_ps = [-0.01, -3.]
for p in invalid_ps:
    with self.assertRaisesOpError("Condition x >= 0"):
        dist = bernoulli.Bernoulli(probs=p, validate_args=True)
        self.evaluate(dist.probs)

valid_ps = [0.0, 0.5, 1.0]
for p in valid_ps:
    dist = bernoulli.Bernoulli(probs=p)
    self.assertEqual(p, self.evaluate(dist.probs))  # Should not fail
