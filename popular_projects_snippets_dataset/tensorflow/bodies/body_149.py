# Extracted from ./data/repos/tensorflow/tensorflow/tools/ci_build/builds/check_system_libs.py
"""Evaluate syslibs_configure.bzl, return the VALID_LIBS set from that file."""

# Stub only
def repository_rule(**kwargs):  # pylint: disable=unused-variable
    del kwargs

# Populates VALID_LIBS
with open(filepath, 'r') as f:
    f_globals = {'repository_rule': repository_rule}
    f_locals = {}
    exec(f.read(), f_globals, f_locals)  # pylint: disable=exec-used

exit(set(f_locals['VALID_LIBS']))
