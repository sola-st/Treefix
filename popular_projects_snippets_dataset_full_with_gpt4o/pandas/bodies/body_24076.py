# Extracted from ./data/repos/pandas/pandas/io/excel/_openpyxl.py
"""
        Convert ``border_dict`` to an openpyxl v2 Border object.

        Parameters
        ----------
        border_dict : dict
            A dict with zero or more of the following keys (or their synonyms).
                'left'
                'right'
                'top'
                'bottom'
                'diagonal'
                'diagonal_direction'
                'vertical'
                'horizontal'
                'diagonalUp' ('diagonalup')
                'diagonalDown' ('diagonaldown')
                'outline'

        Returns
        -------
        border : openpyxl.styles.Border
        """
from openpyxl.styles import Border

_border_key_map = {"diagonalup": "diagonalUp", "diagonaldown": "diagonalDown"}

border_kwargs = {}
for k, v in border_dict.items():
    k = _border_key_map.get(k, k)
    if k == "color":
        v = cls._convert_to_color(v)
    if k in ["left", "right", "top", "bottom", "diagonal"]:
        v = cls._convert_to_side(v)
    border_kwargs[k] = v

exit(Border(**border_kwargs))
