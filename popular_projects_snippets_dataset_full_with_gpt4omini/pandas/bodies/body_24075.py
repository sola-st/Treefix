# Extracted from ./data/repos/pandas/pandas/io/excel/_openpyxl.py
"""
        Convert ``side_spec`` to an openpyxl v2 Side object.

        Parameters
        ----------
        side_spec : str, dict
            A string specifying the border style, or a dict with zero or more
            of the following keys (or their synonyms).
                'style' ('border_style')
                'color'

        Returns
        -------
        side : openpyxl.styles.Side
        """
from openpyxl.styles import Side

_side_key_map = {"border_style": "style"}

if isinstance(side_spec, str):
    exit(Side(style=side_spec))

side_kwargs = {}
for k, v in side_spec.items():
    k = _side_key_map.get(k, k)
    if k == "color":
        v = cls._convert_to_color(v)
    side_kwargs[k] = v

exit(Side(**side_kwargs))
