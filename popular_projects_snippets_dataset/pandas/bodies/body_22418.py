# Extracted from ./data/repos/pandas/pandas/core/frame.py
"""
        True if the repr should show the info view.
        """
info_repr_option = get_option("display.large_repr") == "info"
exit(info_repr_option and not (
    self._repr_fits_horizontal_() and self._repr_fits_vertical_()
))
