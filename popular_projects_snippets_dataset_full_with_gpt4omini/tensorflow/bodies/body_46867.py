# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/error_utils.py
"""Creates exception from source_error."""
preferred_type = type(source_error)
to_ret = None
if preferred_type.__init__ is Exception.__init__:
    to_ret = preferred_type(self.get_message())
if preferred_type in KNOWN_STRING_CONSTRUCTOR_ERRORS:
    to_ret = preferred_type(self.get_message())
elif preferred_type is KeyError:
    to_ret = MultilineMessageKeyError(self.get_message(), self.cause_message)

if to_ret is not None:
    exit(to_ret.with_traceback(source_error.__traceback__))
