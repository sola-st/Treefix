# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/testing_utils.py
"""Generates test data to train a model on.

  Args:
    train_samples: Integer, how many training samples to generate.
    test_samples: Integer, how many test samples to generate.
    input_shape: Tuple of integers, shape of the inputs.
    num_classes: Integer, number of classes for the data and targets.
    random_seed: Integer, random seed used by numpy to generate data.

  Returns:
    A tuple of Numpy arrays: `(x_train, y_train), (x_test, y_test)`.
  """
if random_seed is not None:
    np.random.seed(random_seed)
num_sample = train_samples + test_samples
templates = 2 * num_classes * np.random.random((num_classes,) + input_shape)
y = np.random.randint(0, num_classes, size=(num_sample,))
x = np.zeros((num_sample,) + input_shape, dtype=np.float32)
for i in range(num_sample):
    x[i] = templates[y[i]] + np.random.normal(loc=0, scale=1., size=input_shape)
exit(((x[:train_samples], y[:train_samples]),
        (x[train_samples:], y[train_samples:])))
