# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
"""Creates a model for classifying a hand-written digit.

    Args:
      data_format: Either 'channels_first' or 'channels_last'.
    """
super(Mnist, self).__init__()
if data_format == "channels_first":
    self._input_shape = [-1, 1, 28, 28]
else:
    assert data_format == "channels_last"
    self._input_shape = [-1, 28, 28, 1]

self.conv1 = tf_layers.Conv2D(
    32, 5, padding="same", data_format=data_format, activation=nn.relu)
self.conv2 = tf_layers.Conv2D(
    64, 5, padding="same", data_format=data_format, activation=nn.relu)
self.fc1 = tf_layers.Dense(1024, activation=nn.relu)
self.fc2 = tf_layers.Dense(10)
self.dropout = tf_layers.Dropout(0.4)
self.max_pool2d = tf_layers.MaxPooling2D(
    (2, 2), (2, 2), padding="same", data_format=data_format)
