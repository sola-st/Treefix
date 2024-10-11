# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/models.py
"""Builds a convolutional model with low compute requirements.

  This is roughly the network labeled as 'cnn-one-fstride4' in the
  'Convolutional Neural Networks for Small-footprint Keyword Spotting' paper:
  http://www.isca-speech.org/archive/interspeech_2015/papers/i15_1478.pdf

  Here's the layout of the graph:

  (fingerprint_input)
          v
      [Conv2D]<-(weights)
          v
      [BiasAdd]<-(bias)
          v
        [Relu]
          v
      [MatMul]<-(weights)
          v
      [BiasAdd]<-(bias)
          v
      [MatMul]<-(weights)
          v
      [BiasAdd]<-(bias)
          v
      [MatMul]<-(weights)
          v
      [BiasAdd]<-(bias)
          v

  This produces slightly lower quality results than the 'conv' model, but needs
  fewer weight parameters and computations.

  During training, dropout nodes are introduced after the relu, controlled by a
  placeholder.

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
input_frequency_size = model_settings['fingerprint_width']
input_time_size = model_settings['spectrogram_length']
fingerprint_4d = tf.reshape(fingerprint_input,
                            [-1, input_time_size, input_frequency_size, 1])
first_filter_width = 8
first_filter_height = input_time_size
first_filter_count = 186
first_filter_stride_x = 1
first_filter_stride_y = 1
first_weights = tf.compat.v1.get_variable(
    name='first_weights',
    initializer=tf.compat.v1.truncated_normal_initializer(stddev=0.01),
    shape=[first_filter_height, first_filter_width, 1, first_filter_count])
first_bias = tf.compat.v1.get_variable(
    name='first_bias',
    initializer=tf.compat.v1.zeros_initializer,
    shape=[first_filter_count])
first_conv = tf.nn.conv2d(
    input=fingerprint_4d,
    filters=first_weights,
    strides=[1, first_filter_stride_y, first_filter_stride_x, 1],
    padding='VALID') + first_bias
first_relu = tf.nn.relu(first_conv)
if is_training:
    first_dropout = tf.nn.dropout(first_relu, rate=dropout_rate)
else:
    first_dropout = first_relu
first_conv_output_width = math.floor(
    (input_frequency_size - first_filter_width + first_filter_stride_x) /
    first_filter_stride_x)
first_conv_output_height = math.floor(
    (input_time_size - first_filter_height + first_filter_stride_y) /
    first_filter_stride_y)
first_conv_element_count = int(
    first_conv_output_width * first_conv_output_height * first_filter_count)
flattened_first_conv = tf.reshape(first_dropout,
                                  [-1, first_conv_element_count])
first_fc_output_channels = 128
first_fc_weights = tf.compat.v1.get_variable(
    name='first_fc_weights',
    initializer=tf.compat.v1.truncated_normal_initializer(stddev=0.01),
    shape=[first_conv_element_count, first_fc_output_channels])
first_fc_bias = tf.compat.v1.get_variable(
    name='first_fc_bias',
    initializer=tf.compat.v1.zeros_initializer,
    shape=[first_fc_output_channels])
first_fc = tf.matmul(flattened_first_conv, first_fc_weights) + first_fc_bias
if is_training:
    second_fc_input = tf.nn.dropout(first_fc, rate=dropout_rate)
else:
    second_fc_input = first_fc
second_fc_output_channels = 128
second_fc_weights = tf.compat.v1.get_variable(
    name='second_fc_weights',
    initializer=tf.compat.v1.truncated_normal_initializer(stddev=0.01),
    shape=[first_fc_output_channels, second_fc_output_channels])
second_fc_bias = tf.compat.v1.get_variable(
    name='second_fc_bias',
    initializer=tf.compat.v1.zeros_initializer,
    shape=[second_fc_output_channels])
second_fc = tf.matmul(second_fc_input, second_fc_weights) + second_fc_bias
if is_training:
    final_fc_input = tf.nn.dropout(second_fc, rate=dropout_rate)
else:
    final_fc_input = second_fc
label_count = model_settings['label_count']
final_fc_weights = tf.compat.v1.get_variable(
    name='final_fc_weights',
    initializer=tf.compat.v1.truncated_normal_initializer(stddev=0.01),
    shape=[second_fc_output_channels, label_count])
final_fc_bias = tf.compat.v1.get_variable(
    name='final_fc_bias',
    initializer=tf.compat.v1.zeros_initializer,
    shape=[label_count])
final_fc = tf.matmul(final_fc_input, final_fc_weights) + final_fc_bias
if is_training:
    exit((final_fc, dropout_rate))
else:
    exit(final_fc)
