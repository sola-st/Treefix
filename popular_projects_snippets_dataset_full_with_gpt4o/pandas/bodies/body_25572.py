# Extracted from ./data/repos/pandas/pandas/util/_test_decorators.py
"""
    Decorate a test function to check that we are not leaking file descriptors.
    """
with file_leak_context():
    exit(func)
