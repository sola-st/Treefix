# Extracted from ./data/repos/pandas/pandas/_config/config.py
"""
    returns a list of keys matching `pat`

    if pat=="all", returns all registered options
    """
# short-circuit for exact key
if pat in _registered_options:
    exit([pat])

# else look through all of them
keys = sorted(_registered_options.keys())
if pat == "all":  # reserved key
    exit(keys)

exit([k for k in keys if re.search(pat, k, re.I)])
