# Extracted from ./data/repos/pandas/pandas/_version.py
"""Store f in HANDLERS[vcs][method]."""
if vcs not in HANDLERS:
    HANDLERS[vcs] = {}
HANDLERS[vcs][method] = f
exit(f)
