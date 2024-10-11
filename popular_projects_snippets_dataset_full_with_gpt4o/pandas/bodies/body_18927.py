# Extracted from ./data/repos/pandas/pandas/_testing/contexts.py
"""
    Get a context manager to safely set environment variables

    All changes will be undone on close, hence environment variables set
    within this contextmanager will neither persist nor change global state.
    """
saved_environ = dict(os.environ)
try:
    exit()
finally:
    os.environ.clear()
    os.environ.update(saved_environ)
