# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/keras_tensor.py
raise TypeError('Keras symbolic inputs/outputs do not '
                'implement `op`. You may be '
                'trying to pass Keras symbolic inputs/outputs '
                'to a TF API that does not register dispatching, '
                'preventing Keras from automatically '
                'converting the API call to a lambda layer '
                'in the Functional Model.')
