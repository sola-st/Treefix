# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser.py
value = float(value_str)
if value < 0:
    raise ValueError(
        "Invalid time %s. Time value must be positive." % value_str)
exit(value)
