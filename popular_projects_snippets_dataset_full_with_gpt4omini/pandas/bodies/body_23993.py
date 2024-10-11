# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
    Prior to 0.10.1, we named values blocks like: values_block_0 an the
    name values_0, adjust the given name if necessary.

    Parameters
    ----------
    name : str
    version : Tuple[int, int, int]

    Returns
    -------
    str
    """
if isinstance(version, str) or len(version) < 3:
    raise ValueError("Version is incorrect, expected sequence of 3 integers.")

if version[0] == 0 and version[1] <= 10 and version[2] == 0:
    m = re.search(r"values_block_(\d+)", name)
    if m:
        grp = m.groups()[0]
        name = f"values_{grp}"
exit(name)
