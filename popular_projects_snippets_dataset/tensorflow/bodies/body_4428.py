# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/models.py
"""Builds an SVDF model with low compute requirements.

  This is based in the topology presented in the 'Compressing Deep Neural
  Networks using a Rank-Constrained Topology' paper:
  https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/43813.pdf

  Here's the layout of the graph:

  (fingerprint_input)
          v
        [SVDF]<-(weights)
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

  This model produces lower recognition accuracy than the 'conv' model above,
  but requires fewer weight parameters and, significantly fewer computations.

  During training, dropout nodes are introduced after the relu, controlled by a
  placeholder.

  Args:
    fingerprint_input: TensorFlow node that will output audio feature vectors.
    The node is expected to produce a 2D Tensor of shape:
      [batch, model_settings['fingerprint_width'] *
              model_settings['spectrogram_length']]
    with the features corresponding to the same time slot arranged contiguously,
    and the oldest slot at index [:, 0], and newest at [:, -1].
    model_settings: Dictionary of information about the model.
    is_training: Whether the model is going to be used for training.
    runtime_settings: Dictionary of information about the runtime.

  Returns:
    TensorFlow node outputting logits results, and optionally a dropout
    placeholder.

  Raises:
      ValueError: If the inputs tensor is incorrectly shaped.
  """
if is_training:
    dropout_rate = tf.compat.v1.placeholder(tf.float32, name='dropout_rate')

input_frequency_size = model_settings['fingerprint_width']
input_time_size = model_settings['spectrogram_length']

# Validation.
input_shape = fingerprint_input.get_shape()
if len(input_shape) != 2:
    raise ValueError('Inputs to `SVDF` should have rank == 2.')
if input_shape[-1].value is None:
    raise ValueError('The last dimension of the input to `SVDF` '
                     'should be defined. Found `None`.')
if input_shape[-1].value % input_frequency_size != 0:
    raise ValueError('The last dimension of the input to `SVDF` = {0} must be '
                     'a multiple of the frame size = {1}'.format(
                         input_shape.shape[-1].value, input_frequency_size))

# Set number of units (i.e. nodes) and rank.
rank = 2
num_units = 1280
# Number of filters: pairs of feature and time filters.
num_filters = rank * num_units
# Create the runtime memory: [num_filters, batch, input_time_size]
batch = 1
memory = tf.compat.v1.get_variable(
    initializer=tf.compat.v1.zeros_initializer,
    shape=[num_filters, batch, input_time_size],
    trainable=False,
    name='runtime-memory')
first_time_flag = tf.compat.v1.get_variable(
    name='first_time_flag', dtype=tf.int32, initializer=1)
# Determine the number of new frames in the input, such that we only operate
# on those. For training we do not use the memory, and thus use all frames
# provided in the input.
# new_fingerprint_input: [batch, num_new_frames*input_frequency_size]
if is_training:
    num_new_frames = input_time_size
else:
    window_stride_ms = int(model_settings['window_stride_samples'] * 1000 /
                           model_settings['sample_rate'])
    num_new_frames = tf.cond(
        pred=tf.equal(first_time_flag, 1),
        true_fn=lambda: input_time_size,
        false_fn=lambda: int(runtime_settings['clip_stride_ms'] / window_stride_ms))  # pylint:disable=line-too-long
first_time_flag = 0
new_fingerprint_input = fingerprint_input[
    :, -num_new_frames*input_frequency_size:]
# Expand to add input channels dimension.
new_fingerprint_input = tf.expand_dims(new_fingerprint_input, 2)

# Create the frequency filters.
weights_frequency = tf.compat.v1.get_variable(
    name='weights_frequency',
    initializer=tf.compat.v1.truncated_normal_initializer(stddev=0.01),
    shape=[input_frequency_size, num_filters])
# Expand to add input channels dimensions.
# weights_frequency: [input_frequency_size, 1, num_filters]
weights_frequency = tf.expand_dims(weights_frequency, 1)
# Convolve the 1D feature filters sliding over the time dimension.
# activations_time: [batch, num_new_frames, num_filters]
activations_time = tf.nn.conv1d(input=new_fingerprint_input,
                                filters=weights_frequency,
                                stride=input_frequency_size,
                                padding='VALID')
# Rearrange such that we can perform the batched matmul.
# activations_time: [num_filters, batch, num_new_frames]
activations_time = tf.transpose(a=activations_time, perm=[2, 0, 1])

# Runtime memory optimization.
if not is_training:
    # We need to drop the activations corresponding to the oldest frames, and
    # then add those corresponding to the new frames.
    new_memory = memory[:, :, num_new_frames:]
    new_memory = tf.concat([new_memory, activations_time], 2)
    tf.compat.v1.assign(memory, new_memory)
    activations_time = new_memory

# Create the time filters.
weights_time = tf.compat.v1.get_variable(
    name='weights_time',
    initializer=tf.compat.v1.truncated_normal_initializer(stddev=0.01),
    shape=[num_filters, input_time_size])
# Apply the time filter on the outputs of the feature filters.
# weights_time: [num_filters, input_time_size, 1]
# outputs: [num_filters, batch, 1]
weights_time = tf.expand_dims(weights_time, 2)
outputs = tf.matmul(activations_time, weights_time)
# Split num_units and rank into separate dimensions (the remaining
# dimension is the input_shape[0] -i.e. batch size). This also squeezes
# the last dimension, since it's not used.
# [num_filters, batch, 1] => [num_units, rank, batch]
outputs = tf.reshape(outputs, [num_units, rank, -1])
# Sum the rank outputs per unit => [num_units, batch].
units_output = tf.reduce_sum(input_tensor=outputs, axis=1)
# Transpose to shape [batch, num_units]
units_output = tf.transpose(a=units_output)

# Apply bias.
bias = tf.compat.v1.get_variable(name='bias',
                                 initializer=tf.compat.v1.zeros_initializer,
                                 shape=[num_units])
first_bias = tf.nn.bias_add(units_output, bias)

# Relu.
first_relu = tf.nn.relu(first_bias)

if is_training:
    first_dropout = tf.nn.dropout(first_relu, rate=dropout_rate)
else:
    first_dropout = first_relu

first_fc_output_channels = 256
first_fc_weights = tf.compat.v1.get_variable(
    name='first_fc_weights',
    initializer=tf.compat.v1.truncated_normal_initializer(stddev=0.01),
    shape=[num_units, first_fc_output_channels])
first_fc_bias = tf.compat.v1.get_variable(
    name='first_fc_bias',
    initializer=tf.compat.v1.zeros_initializer,
    shape=[first_fc_output_channels])
first_fc = tf.matmul(first_dropout, first_fc_weights) + first_fc_bias
if is_training:
    second_fc_input = tf.nn.dropout(first_fc, rate=dropout_rate)
else:
    second_fc_input = first_fc
second_fc_output_channels = 256
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
