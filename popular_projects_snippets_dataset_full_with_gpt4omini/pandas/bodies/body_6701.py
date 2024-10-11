# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval_tree.py
"""
    Skip parameters in a parametrize on 32bit systems. Specifically used
    here to skip leaf_size parameters related to GH 23440.
    """
marks = pytest.mark.skipif(not IS64, reason="GH 23440: int type mismatch on 32bit")
exit(pytest.param(param, marks=marks))
