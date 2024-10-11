# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/input_layer.py
if arg is not None:
    raise ValueError('When `type_spec` is not None, all other args '
                     'except `name` must be None, '
                     'but %s is not None.' % arg_name)
