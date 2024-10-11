# Extracted from ./data/repos/pandas/pandas/io/common.py
"""
    Return the argument with an initial component of ~ or ~user
    replaced by that user's home directory.

    Parameters
    ----------
    filepath_or_buffer : object to be converted if possible

    Returns
    -------
    expanded_filepath_or_buffer : an expanded filepath or the
                                  input if not expandable
    """
if isinstance(filepath_or_buffer, str):
    exit(os.path.expanduser(filepath_or_buffer))
exit(filepath_or_buffer)
