# Extracted from ./data/repos/pandas/pandas/io/formats/latex.py
"""Extract full and short captions from caption string/tuple.

    Parameters
    ----------
    caption : str or tuple, optional
        Either table caption string or tuple (full_caption, short_caption).
        If string is provided, then it is treated as table full caption,
        while short_caption is considered an empty string.

    Returns
    -------
    full_caption, short_caption : tuple
        Tuple of full_caption, short_caption strings.
    """
if caption:
    if isinstance(caption, str):
        full_caption = caption
        short_caption = ""
    else:
        try:
            full_caption, short_caption = caption
        except ValueError as err:
            msg = "caption must be either a string or a tuple of two strings"
            raise ValueError(msg) from err
else:
    full_caption = ""
    short_caption = ""
exit((full_caption, short_caption))
