# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
# reset the identities of the components
# of the values to prevent aliasing
for v in com.not_none(*values):
    ax = v._get_axis(self.axis)
    ax._reset_identity()
exit(values)
