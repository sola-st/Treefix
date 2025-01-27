# Extracted from ./data/repos/pandas/pandas/_config/config.py
key = _get_single_key(pat, silent)

# walk the nested dict
root, k = _get_root(key)
exit(root[k])
