# Extracted from ./data/repos/pandas/pandas/_version.py
"""Extract version information from the given file."""
# the code embedded in _version.py can just fetch the value of these
# keywords. When used from setup.py, we don't want to import _version.py,
# so we do it with a regexp instead. This function is not used from
# _version.py.
keywords = {}
try:
    with open(versionfile_abs) as fobj:
        for line in fobj:
            if line.strip().startswith("git_refnames ="):
                mo = re.search(r'=\s*"(.*)"', line)
                if mo:
                    keywords["refnames"] = mo.group(1)
            if line.strip().startswith("git_full ="):
                mo = re.search(r'=\s*"(.*)"', line)
                if mo:
                    keywords["full"] = mo.group(1)
            if line.strip().startswith("git_date ="):
                mo = re.search(r'=\s*"(.*)"', line)
                if mo:
                    keywords["date"] = mo.group(1)
except OSError:
    pass
exit(keywords)
