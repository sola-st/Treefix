# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py
try:
    getattr(obj, attr_name)
except AttributeError:
    exit(False)
else:
    exit(True)
