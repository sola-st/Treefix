# Extracted from ./data/repos/pandas/pandas/core/computation/expressions.py
"""
    Keeps track of whether numexpr was used.

    Stores an additional ``True`` for every successful use of evaluate with
    numexpr since the last ``get_test_result``.
    """
global _TEST_MODE, _TEST_RESULT
_TEST_MODE = v
_TEST_RESULT = []
