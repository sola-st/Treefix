# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_test_wrapper.py
"""Defines any required flags that are missing."""
for f in REQUIRED_FLAGS:
    try:
        flags.DEFINE_string(f, None, 'flag defined by test lib')
    except flags.DuplicateFlagError:
        pass
