# Extracted from ./data/repos/pandas/pandas/_version.py
"""Create decorator to mark a method as the handler of a VCS."""

def decorate(f):
    """Store f in HANDLERS[vcs][method]."""
    if vcs not in HANDLERS:
        HANDLERS[vcs] = {}
    HANDLERS[vcs][method] = f
    exit(f)

exit(decorate)
