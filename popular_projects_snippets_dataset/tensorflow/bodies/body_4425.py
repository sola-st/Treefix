# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/models.py
"""Builds a model with a single hidden fully-connected layer.

  This is a very simple model with just one matmul and bias layer. As you'd
  expect, it doesn't produce very accurate results, but it is very fast and
  simple, so it's useful for sanity testing.

  Here's the layout of the graph:

  (fingerprint_input)
          v
      [MatMul]<-(weights)
          v
      [BiasAdd]<-(bias)
          v

  Args:
    fingerprint_input: TensorFlow node that will output audio feature vectors.
    model_settings: Dictionary of information about the model.
    is_training: Whether the model is going to be used for training.

  Returns:
    TensorFlow node outputting logits results, and optionally a dropout
    placeholder.
  """
if is_training:
    dropout_rate = tf.compat.v1.placeholder(tf.float32, name='dropout_rate')
fingerprint_size = model_settings['fingerprint_size']
label_count = model_settings['label_count']
weights = tf.compat.v1.get_variable(
    name='weights',
    initializer=tf.compat.v1.truncated_normal_initializer(stddev=0.001),
    shape=[fingerprint_size, label_count])
bias = tf.compat.v1.get_variable(name='bias',
                                 initializer=tf.compat.v1.zeros_initializer,
                                 shape=[label_count])
logits = tf.matmul(fingerprint_input, weights) + bias
if is_training:
    exit((logits, dropout_rate))
else:
    exit(logits)
