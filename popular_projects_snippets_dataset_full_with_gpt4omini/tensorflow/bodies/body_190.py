# Extracted from ./data/repos/tensorflow/tensorflow/tools/ci_build/update_version.py
"""Update tensorflow/core/public/version.h."""
replace_string_in_line("#define TF_MAJOR_VERSION %s" % old_version.major,
                       "#define TF_MAJOR_VERSION %s" % new_version.major,
                       VERSION_H)
replace_string_in_line("#define TF_MINOR_VERSION %s" % old_version.minor,
                       "#define TF_MINOR_VERSION %s" % new_version.minor,
                       VERSION_H)
replace_string_in_line("#define TF_PATCH_VERSION %s" % old_version.patch,
                       "#define TF_PATCH_VERSION %s" % new_version.patch,
                       VERSION_H)
replace_string_in_line(
    "#define TF_VERSION_SUFFIX \"%s\"" % old_version.identifier_string,
    "#define TF_VERSION_SUFFIX \"%s\"" % new_version.identifier_string,
    VERSION_H)
