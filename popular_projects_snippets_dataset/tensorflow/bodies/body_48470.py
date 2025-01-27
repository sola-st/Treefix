# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/keras_tensor.py
raise TypeError(
    'Cannot convert a symbolic Keras input/output to a numpy array. '
    'This error may indicate that you\'re trying to pass a symbolic value '
    'to a NumPy call, which is not supported. Or, '
    'you may be trying to pass Keras symbolic inputs/outputs '
    'to a TF API that does not register dispatching, '
    'preventing Keras from automatically '
    'converting the API call to a lambda layer '
    'in the Functional Model.')
