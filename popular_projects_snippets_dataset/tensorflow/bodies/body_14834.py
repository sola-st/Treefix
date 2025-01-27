# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_random_test.py
num_samples = 1000
tol = 0.1  # High tolerance to keep the # of samples low else the test
# takes a long time to run.
np_random.seed(10)
outputs = [np_random.randn(*args) for _ in range(num_samples)]

# Test output shape.
for output in outputs:
    self.assertEqual(output.shape, tuple(args))
    default_dtype = (
        np.float64 if np_dtypes.is_allow_float64() else np.float32)
    self.assertEqual(output.dtype.as_numpy_dtype, default_dtype)

if np.prod(args):  # Don't bother with empty arrays.
    outputs = [output.tolist() for output in outputs]

    # Test that the properties of normal distribution are satisfied.
    mean = np.mean(outputs, axis=0)
    stddev = np.std(outputs, axis=0)
    self.assertAllClose(mean, np.zeros(args), atol=tol)
    self.assertAllClose(stddev, np.ones(args), atol=tol)

    # Test that outputs are different with different seeds.
    np_random.seed(20)
    diff_seed_outputs = [
        np_random.randn(*args).tolist() for _ in range(num_samples)
    ]
    self.assertNotAllClose(outputs, diff_seed_outputs)

    # Test that outputs are the same with the same seed.
    np_random.seed(10)
    same_seed_outputs = [
        np_random.randn(*args).tolist() for _ in range(num_samples)
    ]
    self.assertAllClose(outputs, same_seed_outputs)
