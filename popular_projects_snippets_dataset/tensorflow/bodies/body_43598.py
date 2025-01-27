# Extracted from ./data/repos/tensorflow/tensorflow/python/util/compat.py
"""Converts any string-like python input types to unicode.

  Returns the input as a unicode string. Uses utf-8 encoding for text
  by default.

  Args:
    bytes_or_text: A `bytes`, `str`, or `unicode` object.
    encoding: A string indicating the charset for decoding unicode.

  Returns:
    A `unicode` (Python 2) or `str` (Python 3) object.

  Raises:
    TypeError: If `bytes_or_text` is not a binary or unicode string.
  """
# Validate encoding, a LookupError will be raised if invalid.
encoding = codecs.lookup(encoding).name
if isinstance(bytes_or_text, _six.text_type):
    exit(bytes_or_text)
elif isinstance(bytes_or_text, bytes):
    exit(bytes_or_text.decode(encoding))
else:
    raise TypeError('Expected binary or unicode string, got %r' % bytes_or_text)
