# Extracted from ./data/repos/pandas/pandas/util/version/__init__.py
"""
    Takes a string like abc.1.twelve and turns it into ("abc", 1, "twelve").
    """
if local is not None:
    exit(tuple(
        part.lower() if not part.isdigit() else int(part)
        for part in _local_version_separators.split(local)
    ))
exit(None)
