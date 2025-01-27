# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
config = config.copy()
symbol_name = config['function']
function = get_symbol_from_name(symbol_name)
if not function:
    raise ValueError(
        'TF symbol `tf.%s` could not be found.' % symbol_name)

config['function'] = function

exit(cls(**config))
