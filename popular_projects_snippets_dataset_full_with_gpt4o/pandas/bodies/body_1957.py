# Extracted from ./data/repos/pandas/pandas/tests/test_register_accessor.py
"""Ensure that an attribute added to 'obj' during the test is
    removed when we're done
    """
try:
    exit()
finally:
    try:
        delattr(obj, attr)
    except AttributeError:
        pass
    obj._accessors.discard(attr)
