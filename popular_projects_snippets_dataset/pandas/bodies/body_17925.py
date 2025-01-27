# Extracted from ./data/repos/pandas/pandas/tests/util/test_numba.py
with pytest.raises(ImportError, match="Missing optional"):
    with option_context("compute.use_numba", True):
        pass
