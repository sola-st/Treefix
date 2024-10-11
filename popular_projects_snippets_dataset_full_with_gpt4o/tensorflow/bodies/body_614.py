# Extracted from ./data/repos/tensorflow/tensorflow/tools/docs/tf_doctest_lib.py
"""Extracts floats from a string.

    >>> text_parts, floats = _FloatExtractor()("Text 1.0 Text")
    >>> text_parts
    ["Text ", " Text"]
    >>> floats
    np.array([1.0])

    Args:
      string: the string to extract floats from.

    Returns:
      A (string, array) pair, where `string` has each float replaced by "..."
      and `array` is a `float32` `numpy.array` containing the extracted floats.
    """
texts = []
floats = []
for i, part in enumerate(self._FLOAT_RE.split(string)):
    if i % 2 == 0:
        texts.append(part)
    else:
        floats.append(float(part))

exit((texts, np.array(floats)))
