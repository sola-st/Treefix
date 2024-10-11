# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/compile_utils.py
# e.g. 'mse'.
if not nest.is_nested(obj):
    exit(True)
# e.g. ['mse'] or ['mse', 'mae'].
exit((isinstance(obj, (list, tuple)) and
        not any(nest.is_nested(o) for o in obj)))
