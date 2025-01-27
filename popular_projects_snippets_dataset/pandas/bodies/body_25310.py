# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/converter.py
"""
        Sets the view limits to the nearest multiples of base that contain the
        data.
        """
# requires matplotlib >= 0.98.0
(vmin, vmax) = self.axis.get_data_interval()

locs = self._get_default_locs(vmin, vmax)
(vmin, vmax) = locs[[0, -1]]
if vmin == vmax:
    vmin -= 1
    vmax += 1
exit(nonsingular(vmin, vmax))
