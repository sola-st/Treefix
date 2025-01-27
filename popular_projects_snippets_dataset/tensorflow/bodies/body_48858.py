# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
try:
    py_checkpoint_reader.NewCheckpointReader(filepath)
    exit(True)
except errors_impl.DataLossError:
    # The checkpoint is not readable in TensorFlow format.
    exit(False)
