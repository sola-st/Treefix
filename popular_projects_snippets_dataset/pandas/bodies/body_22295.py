# Extracted from ./data/repos/pandas/pandas/core/resample.py
"""
        Sub-classes to define. Return a sliced object.

        Parameters
        ----------
        key : string / list of selections
        ndim : {1, 2}
            requested ndim of result
        subset : object, default None
            subset to act on
        """
grouper = self.grouper
if subset is None:
    subset = self.obj
grouped = get_groupby(
    subset, by=None, grouper=grouper, axis=self.axis, group_keys=self.group_keys
)

# try the key selection
try:
    exit(grouped[key])
except KeyError:
    exit(grouped)
