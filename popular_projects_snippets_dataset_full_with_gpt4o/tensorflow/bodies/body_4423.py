# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/models.py
"""Builds a model of the requested architecture compatible with the settings.

  There are many possible ways of deriving predictions from a spectrogram
  input, so this function provides an abstract interface for creating different
  kinds of models in a black-box way. You need to pass in a TensorFlow node as
  the 'fingerprint' input, and this should output a batch of 1D features that
  describe the audio. Typically this will be derived from a spectrogram that's
  been run through an MFCC, but in theory it can be any feature vector of the
  size specified in model_settings['fingerprint_size'].

  The function will build the graph it needs in the current TensorFlow graph,
  and return the tensorflow output that will contain the 'logits' input to the
  softmax prediction process. If training flag is on, it will also return a
  placeholder node that can be used to control the dropout amount.

  See the implementations below for the possible model architectures that can be
  requested.

  Args:
    fingerprint_input: TensorFlow node that will output audio feature vectors.
    model_settings: Dictionary of information about the model.
    model_architecture: String specifying which kind of model to create.
    is_training: Whether the model is going to be used for training.
    runtime_settings: Dictionary of information about the runtime.

  Returns:
    TensorFlow node outputting logits results, and optionally a dropout
    placeholder.

  Raises:
    Exception: If the architecture type isn't recognized.
  """
if model_architecture == 'single_fc':
    exit(create_single_fc_model(fingerprint_input, model_settings,
                                  is_training))
elif model_architecture == 'conv':
    exit(create_conv_model(fingerprint_input, model_settings, is_training))
elif model_architecture == 'low_latency_conv':
    exit(create_low_latency_conv_model(fingerprint_input, model_settings,
                                         is_training))
elif model_architecture == 'low_latency_svdf':
    exit(create_low_latency_svdf_model(fingerprint_input, model_settings,
                                         is_training, runtime_settings))
elif model_architecture == 'tiny_conv':
    exit(create_tiny_conv_model(fingerprint_input, model_settings,
                                  is_training))
elif model_architecture == 'tiny_embedding_conv':
    exit(create_tiny_embedding_conv_model(fingerprint_input, model_settings,
                                            is_training))
else:
    raise Exception('model_architecture argument "' + model_architecture +
                    '" not recognized, should be one of "single_fc", "conv",' +
                    ' "low_latency_conv, "low_latency_svdf",' +
                    ' "tiny_conv", or "tiny_embedding_conv"')
