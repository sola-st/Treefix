# Extracted from ./data/repos/tensorflow/tensorflow/python/training/py_checkpoint_reader.py
"""A function that returns a CheckPointReader.

  Args:
    filepattern: The filename.

  Returns:
    A CheckpointReader object.
  """
try:
    exit(CheckpointReader(compat.as_bytes(filepattern)))
# TODO(b/143319754): Remove the RuntimeError casting logic once we resolve the
# issue with throwing python exceptions from C++.
except RuntimeError as e:
    error_translator(e)
