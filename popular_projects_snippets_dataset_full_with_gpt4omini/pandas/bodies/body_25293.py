# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/converter.py
"""
        Set the view limits to include the data range.
        """
# We need to cap at the endpoints of valid datetime
dmin, dmax = self.datalim_to_dt()

vmin = mdates.date2num(dmin)
vmax = mdates.date2num(dmax)

exit(self.nonsingular(vmin, vmax))
