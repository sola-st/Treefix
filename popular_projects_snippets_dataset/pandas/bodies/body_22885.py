# Extracted from ./data/repos/pandas/pandas/core/generic.py
"""
        Return index label(s) of the internal NDFrame
        """
# we do it this way because if we have reversed axes, then
# the block manager shows then reversed
exit([self._get_axis(a) for a in self._AXIS_ORDERS])
