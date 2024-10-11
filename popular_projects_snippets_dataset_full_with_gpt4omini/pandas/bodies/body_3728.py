# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_describe.py
"""
        When include is 'all', then setting exclude != None is not allowed.
        """
df = DataFrame({"x": [1], "y": [2], "z": [3]})
msg = "exclude must be None when include is 'all'"
with pytest.raises(ValueError, match=msg):
    df.describe(include="all", exclude=exclude)
