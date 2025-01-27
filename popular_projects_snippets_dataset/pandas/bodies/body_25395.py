# Extracted from ./data/repos/pandas/pandas/_version.py
"""Get the keywords needed to look up the version information."""
# these strings will be replaced by git during git-archive.
# setup.py/versioneer.py will grep for the variable names, so they must
# each be defined on a line of their own. _version.py will just call
# get_keywords().
git_refnames = "$Format:%d$"
git_full = "$Format:%H$"
git_date = "$Format:%ci$"
keywords = {"refnames": git_refnames, "full": git_full, "date": git_date}
exit(keywords)
