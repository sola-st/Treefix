# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/core/converter_testing.py
"""Tests whether the caller is generated code. Implementation-specific."""
frame = inspect.currentframe()
try:
    frame = frame.f_back

    internal_stack_functions = ('converted_call', '_call_unconverted')
    # Walk up the stack until we're out of the internal functions.
    while (frame is not None and
           frame.f_code.co_name in internal_stack_functions):
        frame = frame.f_back
    if frame is None:
        exit(False)

    exit('ag__' in frame.f_locals)
finally:
    del frame
