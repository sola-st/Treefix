# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/models.py
"""Builds a convolutional model aimed at microcontrollers.

  Devices like DSPs and microcontrollers can have very small amounts of
  memory and limited processing power. This model is designed to use less
  than 20KB of working RAM, and fit within 32KB of read-only (flash) memory.

  Here's the layout of the graph:

  (fingerprint_input)
          v
      [Conv2D]<-(weights)
          v
      [BiasAdd]<-(bias)
          v
        [Relu]
          v
      [Conv2D]<-(weights)
          v
      [BiasAdd]<-(bias)
          v
        [Relu]
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

  This doesn't produce particularly accurate results, but it's designed to be
  used as the first stage of a pipeline, running on a low-energy piece of
  hardware that can always be on, and then wake higher-power chips when a
  possible utterance has been found, so that more accurate analysis can be done.

  During training, a dropout node is introduced after the relu, controlled by a
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
first_filter_height = 10
first_filter_count = 8
first_weights = tf.compat.v1.get_variable(
    name='first_weights',
    initializer=tf.compat.v1.truncated_normal_initializer(stddev=0.01),
    shape=[first_filter_height, first_filter_width, 1, first_filter_count])
first_bias = tf.compat.v1.get_variable(
    name='first_bias',
    initializer=tf.compat.v1.zeros_initializer,
    shape=[first_filter_count])
first_conv_stride_x = 2
first_conv_stride_y = 2

first_conv = tf.nn.conv2d(
    input=fingerprint_4d, filters=first_weights,
    strides=[1, first_conv_stride_y, first_conv_stride_x, 1],
    padding='SAME') + first_bias
first_relu = tf.nn.relu(first_conv)
if is_training:
    first_dropout = tf.nn.dropout(first_relu, rate=dropout_rate)

else:
    first_dropout = first_relu

second_filter_width = 8
second_filter_height = 10
second_filter_count = 8
second_weights = tf.compat.v1.get_variable(
    name='second_weights',
    initializer=tf.compat.v1.truncated_normal_initializer(stddev=0.01),
    shape=[
        second_filter_height, second_filter_width, first_filter_count,
        second_filter_count
    ])
second_bias = tf.compat.v1.get_variable(
    name='second_bias',
    initializer=tf.compat.v1.zeros_initializer,
    shape=[second_filter_count])
second_conv_stride_x = 8
second_conv_stride_y = 8
second_conv = tf.nn.conv2d(
    input=first_dropout, filters=second_weights,
    strides=[1, second_conv_stride_y, second_conv_stride_x, 1],
    padding='SAME') + second_bias
second_relu = tf.nn.relu(second_conv)
if is_training:
    second_dropout = tf.nn.dropout(second_relu, rate=dropout_rate)
else:
    second_dropout = second_relu

second_dropout_shape = second_dropout.get_shape()
second_dropout_output_width = second_dropout_shape[2]
second_dropout_output_height = second_dropout_shape[1]
second_dropout_element_count = int(second_dropout_output_width *
                                   second_dropout_output_height *
                                   second_filter_count)
flattened_second_dropout = tf.reshape(second_dropout,
                                      [-1, second_dropout_element_count])
label_count = model_settings['label_count']
final_fc_weights = tf.compat.v1.get_variable(
    name='final_fc_weights',
    initializer=tf.compat.v1.truncated_normal_initializer(stddev=0.01),
    shape=[second_dropout_element_count, label_count])
final_fc_bias = tf.compat.v1.get_variable(
    name='final_fc_bias',
    initializer=tf.compat.v1.zeros_initializer,
    shape=[label_count])
final_fc = (
    tf.matmul(flattened_second_dropout, final_fc_weights) + final_fc_bias)
if is_training:
    exit((final_fc, dropout_rate))
else:
    exit(final_fc)
