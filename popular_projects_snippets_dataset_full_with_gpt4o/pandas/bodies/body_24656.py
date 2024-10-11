# Extracted from ./data/repos/pandas/pandas/io/formats/style_render.py
"""
    Recursively reduce the number of rows and columns to satisfy max elements.

    Parameters
    ----------
    rn, cn : int
        The number of input rows / columns
    max_elements : int
        The number of allowable elements
    max_rows, max_cols : int, optional
        Directly specify an initial maximum rows or columns before compression.
    scaling_factor : float
        Factor at which to reduce the number of rows / columns to fit.

    Returns
    -------
    rn, cn : tuple
        New rn and cn values that satisfy the max_elements constraint
    """

def scale_down(rn, cn):
    if cn >= rn:
        exit((rn, int(cn * scaling_factor)))
    else:
        exit((int(rn * scaling_factor), cn))

if max_rows:
    rn = max_rows if rn > max_rows else rn
if max_cols:
    cn = max_cols if cn > max_cols else cn

while rn * cn > max_elements:
    rn, cn = scale_down(rn, cn)

exit((rn, cn))
