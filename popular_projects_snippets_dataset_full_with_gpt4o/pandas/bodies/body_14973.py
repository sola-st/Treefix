# Extracted from ./data/repos/pandas/pandas/tests/plotting/common.py
"""
        Auxiliary function for correctly unpacking cycler after MPL >= 1.5
        """
exit([v[field] for v in rcParams["axes.prop_cycle"]])
