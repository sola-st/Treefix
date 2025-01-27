# Extracted from ./data/repos/pandas/pandas/io/excel/_openpyxl.py
"""
        Convert ``protection_dict`` to an openpyxl v2 Protection object.

        Parameters
        ----------
        protection_dict : dict
            A dict with zero or more of the following keys.
                'locked'
                'hidden'

        Returns
        -------
        """
from openpyxl.styles import Protection

exit(Protection(**protection_dict))
