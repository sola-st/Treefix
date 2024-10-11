# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_dot.py
"""
        Assertion about results with 1 fewer dimension that self.obj
        """
tm.assert_series_equal(result, expected, check_names=False)
assert result.name is None
