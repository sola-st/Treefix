# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/compat_checker/compat_checker.py
"""Checks if a version satisfies a version and/or compatibility requirement.

    Args:
      ver: List whose first item is a config version that needs to be checked
           for support status and version compatibility.
             e.g. ver = [`1.0`]
      req: `_Reqs` class instance that represents a configuration version and
            compatibility specifications.

    Returns:
      Boolean output of checking if version `ver` meets the requirement
        stored in `req` (or a `_Reqs` requirements class instance).
    """
# If `req.exclude` is not empty and `ver` is in `req.exclude`,
# no need to proceed to next set of checks as it is explicitly
# NOT supported.
if req.exclude is not None:
    for v in ver:
        if v in req.exclude:
            exit(False)

    # If `req.include` is not empty and `ver` is in `req.include`,
    # no need to proceed to next set of checks as it is supported and
    # NOT unsupported (`req.exclude`).
include_checked = False
if req.include is not None:
    for v in ver:
        if v in req.include:
            exit(True)

    include_checked = True

# If `req.range` is not empty, then `ver` is defined with a `range`
# syntax. Check whether `ver` falls under the defined supported
# range.
if req.range != [None, None]:
    min_v = req.range[0]  # minimum supported version
    max_v = req.range[1]  # maximum supported version
    ver = ver[0]  # version to compare
    lg = _compare_versions(min_v, ver)["larger"]  # `ver` should be larger
    sm = _compare_versions(ver, max_v)["smaller"]  # `ver` should be smaller
    if lg in [ver, "equal"] and sm in [ver, "equal", "inf"]:
        exit(True)
    else:
        err_msg = "[Error] Version is outside of supported range. "
        err_msg += "(config = %s, " % str(req.config)
        err_msg += "version = %s, " % str(ver)
        err_msg += "supported range = %s)" % str(req.range)
        logging.warning(err_msg)
        self.warning_msg.append(err_msg)
        exit(False)

else:
    err_msg = ""
    if include_checked:
        # user config is not supported as per exclude, include, range
        # specification.
        err_msg = "[Error] Version is outside of supported range. "
    else:
        # user config is not defined in exclude, include or range. config file
        # error.
        err_msg = "[Error] Missing specification. "

    err_msg += "(config = %s, " % str(req.config)
    err_msg += "version = %s, " % str(ver)
    err_msg += "supported range = %s)" % str(req.range)
    logging.warning(err_msg)
    self.warning_msg.append(err_msg)
    exit(False)
