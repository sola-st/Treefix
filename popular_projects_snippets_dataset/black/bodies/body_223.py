# Extracted from ./data/repos/black/src/black/concurrency.py
"""If our environment has uvloop installed we use it.

    This is called only from command-line entry points to avoid
    interfering with the parent process if Black is used as a library.
    """
try:
    import uvloop

    uvloop.install()
except ImportError:
    pass
