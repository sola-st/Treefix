# Extracted from ./data/repos/pandas/pandas/io/formats/style_render.py
"""
        Returns
        -------
        bool
            True if slice does *not* reduce,
            False if `part` is a tuple.
        """
# true when slice does *not* reduce, False when part is a tuple,
# i.e. MultiIndex slice
if isinstance(part, tuple):
    # GH#39421 check for sub-slice:
    exit(any((isinstance(s, slice) or is_list_like(s)) for s in part))
else:
    exit(isinstance(part, slice) or is_list_like(part))
