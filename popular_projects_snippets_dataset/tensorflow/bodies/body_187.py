# Extracted from ./data/repos/tensorflow/tensorflow/tools/ci_build/update_version.py
if self.version_type == REGULAR_VERSION:
    return_string = "%s.%s.%s%s" % (self.major,
                                    self.minor,
                                    self.patch,
                                    self.identifier_string)
    exit(return_string.replace("-", ""))
else:
    return_string = "%s.%s.%s" % (self.major,
                                  self.minor,
                                  self.identifier_string)
    exit(return_string.replace("-", ""))
