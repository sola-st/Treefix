# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder.py
"""Registers a codec to use for encoding/decoding.

  Args:
    x: The codec object to register. The object must implement can_encode,
      do_encode, can_decode, and do_decode. See the various _*Codec classes for
      examples.
  """
_codecs.append(x)
