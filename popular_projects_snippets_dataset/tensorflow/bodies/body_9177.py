# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/integration_test/profiler_api_test.py
"""Set up a MNIST Keras model for testing purposes.

  Builds a MNIST Keras model and returns model information.

  Returns:
    A tuple of (batch_size, steps, train_dataset, mode)
  """
context.set_log_device_placement(True)
batch_size = 64
steps = 2
with collective_strategy.CollectiveAllReduceStrategy().scope():
    # TODO(b/142509827): In rare cases this errors out at C++ level with the
    # "Connect failed" error message.
    train_ds, _ = mnist_testing_utils.mnist_synthetic_dataset(batch_size, steps)
    model = mnist_testing_utils.get_mnist_model((28, 28, 1))
exit((batch_size, steps, train_ds, model))
