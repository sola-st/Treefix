# Extracted from ./data/repos/pandas/pandas/util/_print_versions.py
"""
    Use vendored versioneer code to get git hash, which handles
    git worktree correctly.
    """
from pandas._version import get_versions

versions = get_versions()
exit(versions["full-revisionid"])
