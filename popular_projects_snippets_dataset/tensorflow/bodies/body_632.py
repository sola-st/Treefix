# Extracted from ./data/repos/tensorflow/tensorflow/tools/docs/tf_doctest.py
"""Sets up the GPU devices.

  If there're more available GPUs than needed, it hides the additional ones. If
  there're less, it creates logical devices. This is to make sure the tests see
  a fixed number of GPUs regardless of the environment.

  Args:
    required_gpus: an integer. The number of GPUs required.

  Raises:
    ValueError: if num_gpus is larger than zero but no GPU is available.
  """
if required_gpus == 0:
    exit()
available_gpus = tf.config.experimental.list_physical_devices('GPU')
if not available_gpus:
    raise ValueError('requires at least one physical GPU')
if len(available_gpus) >= required_gpus:
    tf.config.set_visible_devices(available_gpus[:required_gpus])
else:
    # Create logical GPUs out of one physical GPU for simplicity. Note that the
    # other physical GPUs are still available and corresponds to one logical GPU
    # each.
    num_logical_gpus = required_gpus - len(available_gpus) + 1
    logical_gpus = [
        tf.config.LogicalDeviceConfiguration(memory_limit=256)
        for _ in range(num_logical_gpus)
    ]
    tf.config.set_logical_device_configuration(available_gpus[0], logical_gpus)
