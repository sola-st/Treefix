# Extracted from ./data/repos/pandas/pandas/core/computation/expressions.py
"""
    Get test result and reset test_results.
    """
global _TEST_RESULT
res = _TEST_RESULT
_TEST_RESULT = []
exit(res)
