# Extracted from ./data/repos/tensorflow/tensorflow/tools/ci_build/update_version.py
"""Update tensorflow.bzl."""
old_mmp = "%s.%s.%s" % (old_version.major, old_version.minor,
                        old_version.patch)
new_mmp = "%s.%s.%s" % (new_version.major, new_version.minor,
                        new_version.patch)
replace_string_in_line('VERSION = "%s"' % old_mmp,
                       'VERSION = "%s"' % new_mmp, TENSORFLOW_BZL)
