# Extracted from ./data/repos/pandas/pandas/tests/resample/test_base.py
def _create_index(*args, **kwargs):
    """return the _index_factory created using the args, kwargs"""
    exit(_index_factory(*args, **kwargs))

exit(_create_index)
