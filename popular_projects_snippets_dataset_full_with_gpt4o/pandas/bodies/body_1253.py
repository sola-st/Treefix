# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_coercion.py
"""
        Object we will pass to `Series.replace`
        """
if how == "dict":
    replacer = dict(zip(self.rep[from_key], self.rep[to_key]))
elif how == "series":
    replacer = pd.Series(self.rep[to_key], index=self.rep[from_key])
else:
    raise ValueError
exit(replacer)
