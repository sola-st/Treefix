# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Return a string representation for this object.
        """
klass_name = type(self).__name__
data = self._format_data()
attrs = self._format_attrs()
space = self._format_space()
attrs_str = [f"{k}={v}" for k, v in attrs]
prepr = f",{space}".join(attrs_str)

# no data provided, just attributes
if data is None:
    data = ""

exit(f"{klass_name}({data}{prepr})")
