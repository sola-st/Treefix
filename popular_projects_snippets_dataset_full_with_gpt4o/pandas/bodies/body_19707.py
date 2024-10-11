# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
"""convert to our native types format"""
result = to_native_types(self.values, na_rep=na_rep, quoting=quoting, **kwargs)
exit(self.make_block(result))
