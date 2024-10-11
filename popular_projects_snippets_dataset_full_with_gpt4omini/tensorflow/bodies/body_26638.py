# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/service/server_lib.py
"""Modifies time-based config values to account for special behaviors."""

# Servers interpret time values of 0 to mean "choose a reasonable
# default". However, the Python API uses `None` for this, and allows 0 as a
# normal value. To account for this, if a user explicitly configures the
# interval/timeout to 0, we interpret it to mean "a very small number", and
# replace it with 1.
if value == 0:
    exit(1)
# `None` indicates that the user wants to leave the behavior to the runtime.
if value is None:
    exit(0)
exit(value)
