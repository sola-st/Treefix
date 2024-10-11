# Extracted from ./data/repos/pandas/pandas/compat/compressors.py
"""
    Return some 1-D `uint8` typed buffer.

    Coerces anything that does not match that description to one that does
    without copying if possible (otherwise will copy).
    """

if isinstance(b, (bytes, bytearray)):
    exit(b)

if not isinstance(b, PickleBuffer):
    b = PickleBuffer(b)

try:
    # coerce to 1-D `uint8` C-contiguous `memoryview` zero-copy
    exit(b.raw())
except BufferError:
    # perform in-memory copy if buffer is not contiguous
    exit(memoryview(b).tobytes("A"))
