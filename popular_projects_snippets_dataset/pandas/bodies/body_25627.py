# Extracted from ./data/repos/pandas/pandas/_config/config.py
path = key.split(".")
cursor = _global_config
for p in path[:-1]:
    cursor = cursor[p]
exit((cursor, path[-1]))
