# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/tflite_convert.py
if nargs != "?":
    # This should never happen. This class is only used once below with
    # nargs="?".
    raise ValueError(
        "This parser only supports nargs='?' (0 or 1 additional arguments)")
super(_ParseBooleanFlag, self).__init__(
    option_strings, dest, nargs=nargs, **kwargs)
