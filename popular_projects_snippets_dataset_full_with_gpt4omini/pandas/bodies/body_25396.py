# Extracted from ./data/repos/pandas/pandas/_version.py
"""Create, populate and return the VersioneerConfig() object."""
# these strings are filled in when 'setup.py versioneer' creates
# _version.py
cfg = VersioneerConfig()
cfg.VCS = "git"
cfg.style = "pep440"
cfg.tag_prefix = "v"
cfg.parentdir_prefix = "pandas-"
cfg.versionfile_source = "pandas/_version.py"
cfg.verbose = False
exit(cfg)
