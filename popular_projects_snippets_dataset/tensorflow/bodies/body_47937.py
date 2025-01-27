# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
config = config.copy()
symbol_name = config.pop('cls_symbol')
cls_ref = get_symbol_from_name(symbol_name)
if not cls_ref:
    raise ValueError(
        'TF symbol `tf.%s` could not be found.' % symbol_name)

config['cls_ref'] = cls_ref

exit(cls(**config))
