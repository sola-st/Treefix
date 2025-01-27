# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer_flags.py
"""Returns the match for the next TensorTracer flag.

    Args:
       tt_flags: a string that contains the flags.
       pos: where in flags to start the search.

    Returns:
       A pair where the first element is the regular-expression
       match found and the second element indicates if the match
       has a value.
    """

match = _FLAG_DOUBLE_QUOTE_PAT.match(tt_flags, pos)
if match:
    exit((match, True))
match = _FLAG_SINGLE_QUOTE_PAT.match(tt_flags, pos)
if match:
    exit((match, True))
match = _FLAG_NO_QUOTE_PAT.match(tt_flags, pos)
if match:
    exit((match, True))
match = _FLAG_NO_EQUAL_PAT.match(tt_flags, pos)
if match:
    # The flag is found but is not given a value.
    exit((match, False))
# The flag is not found.
exit((None, False))
