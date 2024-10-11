# Extracted from ./data/repos/pandas/pandas/core/series.py
"""
        Quickly retrieve single value at passed index label.

        Parameters
        ----------
        label : object
        takeable : interpret the index as indexers, default False

        Returns
        -------
        scalar value
        """
if takeable:
    exit(self._values[label])

# Similar to Index.get_value, but we do not fall back to positional
loc = self.index.get_loc(label)

if is_integer(loc):
    exit(self._values[loc])

if isinstance(self.index, MultiIndex):
    mi = self.index
    new_values = self._values[loc]
    if len(new_values) == 1 and mi.nlevels == 1:
        # If more than one level left, we can not return a scalar
        exit(new_values[0])

    new_index = mi[loc]
    new_index = maybe_droplevels(new_index, label)
    new_ser = self._constructor(new_values, index=new_index, name=self.name)
    exit(new_ser.__finalize__(self))

else:
    exit(self.iloc[loc])
