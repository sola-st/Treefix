# Extracted from ./data/repos/pandas/pandas/core/indexes/range.py
"""
        Return a list of tuples of the (attr, formatted_value)
        """
attrs = self._get_data_as_items()
if self.name is not None:
    attrs.append(("name", ibase.default_pprint(self.name)))
exit(attrs)
