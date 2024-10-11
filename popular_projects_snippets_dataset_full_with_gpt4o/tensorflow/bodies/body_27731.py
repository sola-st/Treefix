# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/sample_from_datasets_test.py
random_seed.set_random_seed(1619)
num_samples = 5000
rand_probs = self._normalize(np.random.random_sample((5,)))

# Use chi-squared test to assert that the observed distribution matches the
# expected distribution. Based on the implementation in
# "third_party/tensorflow/python/kernel_tests/multinomial_op_test.py".
for probs in [[.85, .05, .1], rand_probs, [1.]]:
    weights = _get_weights_of_type(np.asarray(probs), weights_type)
    classes = len(probs)

    # Create a dataset that samples each integer in `[0, num_datasets)`
    # with probability given by `weights[i]`.
    dataset = dataset_ops.Dataset.sample_from_datasets([
        dataset_ops.Dataset.from_tensors(i).repeat() for i in range(classes)
    ], weights)
    dataset = dataset.take(num_samples)

    next_element = self.getNext(dataset, requires_initialization=True)
    freqs = np.zeros([classes])
    for _ in range(num_samples):
        freqs[self.evaluate(next_element())] += 1
    with self.assertRaises(errors.OutOfRangeError):
        self.evaluate(next_element())

    self.assertLess(self._chi2(probs, freqs / num_samples), 1e-2)
