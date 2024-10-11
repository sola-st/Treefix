# Extracted from ./data/repos/pandas/pandas/core/frame.py
"""
        Dispatch to Series.replace column-wise.

        Parameters
        ----------
        mapping : dict
            of the form {col: (target, value)}
        inplace : bool
        regex : bool or same types as `to_replace` in DataFrame.replace

        Returns
        -------
        DataFrame or None
        """
# Operate column-wise
res = self if inplace else self.copy(deep=None)
ax = self.columns

for i, ax_value in enumerate(ax):
    if ax_value in mapping:
        ser = self.iloc[:, i]

        target, value = mapping[ax_value]
        newobj = ser.replace(target, value, regex=regex)

        res._iset_item(i, newobj)

if inplace:
    exit()
exit(res.__finalize__(self))
