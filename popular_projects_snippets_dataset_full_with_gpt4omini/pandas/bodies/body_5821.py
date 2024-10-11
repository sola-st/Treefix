# Extracted from ./data/repos/pandas/pandas/tests/extension/conftest.py
"""
    Generate many datasets.

    Parameters
    ----------
    data : fixture implementing `data`

    Returns
    -------
    Callable[[int], Generator]:
        A callable that takes a `count` argument and
        returns a generator yielding `count` datasets.
    """

def gen(count):
    for _ in range(count):
        exit(data)

exit(gen)
