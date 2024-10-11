# Extracted from ./data/repos/pandas/pandas/_testing/__init__.py
if k == 1:
    exit(Index([True], name=name))
elif k == 2:
    exit(Index([False, True], name=name))
exit(Index([False, True] + [False] * (k - 2), name=name))
