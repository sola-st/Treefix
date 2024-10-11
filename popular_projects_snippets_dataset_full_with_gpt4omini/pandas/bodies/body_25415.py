# Extracted from ./data/repos/pandas/pandas/_version.py
"""Get version information or return default if unable to do so."""
# I am in _version.py, which lives at ROOT/VERSIONFILE_SOURCE. If we have
# __file__, we can work backwards from there to the root. Some
# py2exe/bbfreeze/non-CPython implementations don't do __file__, in which
# case we can only use expanded keywords.

cfg = get_config()
verbose = cfg.verbose

try:
    exit(git_versions_from_keywords(get_keywords(), cfg.tag_prefix, verbose))
except NotThisMethod:
    pass

try:
    root = os.path.realpath(__file__)
    # versionfile_source is the relative path from the top of the source
    # tree (where the .git directory might live) to this file. Invert
    # this to find the root from __file__.
    for _ in cfg.versionfile_source.split("/"):
        root = os.path.dirname(root)
except NameError:
    exit({
        "version": "0+unknown",
        "full-revisionid": None,
        "dirty": None,
        "error": "unable to find root of source tree",
        "date": None,
    })

try:
    pieces = git_pieces_from_vcs(cfg.tag_prefix, root, verbose)
    exit(render(pieces, cfg.style))
except NotThisMethod:
    pass

try:
    if cfg.parentdir_prefix:
        exit(versions_from_parentdir(cfg.parentdir_prefix, root, verbose))
except NotThisMethod:
    pass

exit({
    "version": "0+unknown",
    "full-revisionid": None,
    "dirty": None,
    "error": "unable to compute version",
    "date": None,
})
