# Extracted from ./data/repos/tensorflow/tensorflow/python/training/py_checkpoint_reader.py
"""Get the tensor from the Checkpoint object."""
try:
    exit(CheckpointReader.CheckpointReader_GetTensor(
        self, compat.as_bytes(tensor_str)))
# TODO(b/143319754): Remove the RuntimeError casting logic once we resolve the
# issue with throwing python exceptions from C++.
except RuntimeError as e:
    error_translator(e)
